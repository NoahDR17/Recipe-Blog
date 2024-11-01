from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Recipe, Review 
from .forms import RecipeForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View

class AddRecipe(LoginRequiredMixin, CreateView):
    """ Add Recipe View """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    context_object_name = "recipes"
    success_url = '/recipes/recipes/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Recipe created successfully!')
        return super(AddRecipe, self).form_valid(form)

class RecipeListView(ListView):
    """ View to list all recipes """
    model = Recipe
    template_name = 'recipes/recipe_list.html' 
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        meal_type = self.request.GET.get('meal_type')

        if meal_type:
            queryset = queryset.filter(meal_type=meal_type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_type = self.request.GET.get('meal_type')
        context['meal_type'] = meal_type
        context['meal_type_choices'] = Recipe.MEAL_TYPE_CHOICES
        return context

class RecipeDetailView(DetailView):
    """ View to view recipe details"""
    model = Recipe
    template_name = 'recipes/recipe_detail.html'  
    context_object_name = 'recipe'  

@login_required
def profile_view(request):
    """ View to display user profile with their recipes """
    user_recipes = Recipe.objects.filter(author=request.user)  
    return render(request, 'recipes/profile.html', {'user': request.user, 'user_recipes': user_recipes})


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'recipes/edit_recipe.html'
    fields = ['title', 'description', 'ingredients', 'instructions', 'calories']
    context_object_name = 'recipe'

    def form_valid(self, form):
        messages.success(self.request, 'Recipe updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    context_object_name = 'recipe'

    def get_success_url(self):
        messages.success(self.request, 'Recipe deleted successfully!')
        return reverse_lazy('recipe_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.review_set.all().delete()
        self.object.delete()
        return redirect(self.get_success_url())
        
class RateRecipeView(LoginRequiredMixin, View):
    def post(self, request, recipe_id):
        rating_value = request.POST.get('rating')
        recipe = get_object_or_404(Recipe, id=recipe_id)


        Review.objects.update_or_create(
            user=request.user,
            recipe=recipe,
            defaults={'rating': rating_value}
        )
        messages.success(request, 'Your rating has been submitted successfully!')
        return redirect('recipe_detail', pk=recipe_id)