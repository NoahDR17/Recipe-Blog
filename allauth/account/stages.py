from typing import Optional

from django.http import HttpResponseRedirect
from django.urls import reverse

from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.app_settings import EmailVerificationMethod
from allauth.account.models import EmailAddress
from allauth.core.internal.httpkit import headed_redirect_response
from allauth.utils import import_callable


class LoginStage:
    key: str  # Set in subclasses
    urlname: Optional[str] = None

    def __init__(self, controller, request, login):
        if not self.key:
            raise ValueError()
        self.controller = controller
        self.request = request
        self.login = login
        self.state = (
            self.login.state.setdefault("stages", {})
            .setdefault(self.key, {})
            .setdefault("data", {})
        )

    def handle(self):
        return None, True

    def exit(self):
        from allauth.account.internal.flows.login import resume_login

        self.controller.set_handled(self.key)
        return resume_login(self.request, self.login)

    def abort(self):
        from allauth.account.internal.stagekit import clear_login

        clear_login(self.request)
        return HttpResponseRedirect(reverse("account_login"))

    def is_resumable(self, request):
        return True


class LoginStageController:
    def __init__(self, request, login):
        self.request = request
        self.login = login
        self.state = self.login.state.setdefault("stages", {})

    @classmethod
    def enter(cls, request, stage_key):
        from allauth.account.internal.stagekit import unstash_login

        login = unstash_login(request, peek=True)
        if not login:
            return None
        ctrl = LoginStageController(request, login)
        if ctrl.state.get("current") != stage_key:
            return None
        stages = ctrl.get_stages()
        for stage in stages:
            if stage.key == stage_key:
                return stage
        return None

    def set_current(self, stage_key):
        self.state["current"] = stage_key

    def is_handled(self, stage_key):
        return self.state.get(stage_key, {}).get("handled", False)

    def set_handled(self, stage_key):
        stage_state = self.state.setdefault(stage_key, {})
        stage_state["handled"] = True

    def get_pending_stage(self) -> Optional[LoginStage]:
        ret = None
        stages = self.get_stages()
        for stage in stages:
            if self.is_handled(stage.key):
                continue
            ret = stage
            break
        return ret

    def get_stages(self):
        stages = []
        adapter = get_adapter(self.request)
        paths = adapter.get_login_stages()
        for path in paths:
            cls = import_callable(path)
            stage = cls(self, self.request, self.login)
            stages.append(stage)
        return stages

    def handle(self):
        from allauth.account.internal.stagekit import clear_login, stash_login

        stages = self.get_stages()
        for stage in stages:
            if self.is_handled(stage.key):
                continue
            self.set_current(stage.key)
            response, cont = stage.handle()
            if response:
                if cont:
                    stash_login(self.request, self.login)
                else:
                    clear_login(self.request)
                return response
            else:
                assert cont
                self.set_handled(stage.key)
        clear_login(self.request)


class EmailVerificationStage(LoginStage):
    key = "verify_email"
    urlname = "account_email_verification_sent"

    def is_resumable(self, request):
        return app_settings.EMAIL_VERIFICATION_BY_CODE_ENABLED

    def handle(self):
        from allauth.account.utils import (
            has_verified_email,
            send_email_confirmation,
        )

        response, cont = None, True
        login = self.login
        email_verification = login.email_verification
        if email_verification == EmailVerificationMethod.NONE:
            pass
        elif email_verification == EmailVerificationMethod.OPTIONAL:
            # In case of OPTIONAL verification: send on signup.
            if not has_verified_email(login.user, login.email) and login.signup:
                send_email_confirmation(
                    self.request, login.user, signup=login.signup, email=login.email
                )
        elif email_verification == EmailVerificationMethod.MANDATORY:
            if not has_verified_email(login.user, login.email):
                send_email_confirmation(
                    self.request, login.user, signup=login.signup, email=login.email
                )
                response = get_adapter().respond_email_verification_sent(
                    self.request, login.user
                )
        return response, cont


class LoginByCodeStage(LoginStage):
    key = "login_by_code"
    urlname = "account_confirm_login_code"

    def handle(self):
        from allauth.account.internal.flows import login_by_code

        user, data = login_by_code.get_pending_login(
            self.request, self.login, peek=True
        )
        login_by_code_required = get_adapter().is_login_by_code_required(self.login)
        if data is None and not login_by_code_required:
            # No pending login, just continue.
            return None, True
        elif data is None and login_by_code_required:
            email = EmailAddress.objects.get_primary_email(self.login.user)
            if not email:
                # No way of contacting the user.. cannot meet the
                # requirements. Abort.
                return headed_redirect_response("account_login"), False
            login_by_code.request_login_code(self.request, email, login=self.login)

        response = headed_redirect_response("account_confirm_login_code")
        return response, True