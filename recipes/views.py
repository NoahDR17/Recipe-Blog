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
    """ View to add a new recipe """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    context_object_name = "recipes"
    success_url = '/recipes/recipes/'

    def form_valid(self, form):
        """ Sets the author to the logged-in user and displays a success message """
        form.instance.author = self.request.user
        messages.success(self.request, 'Recipe created successfully!')
        return super(AddRecipe, self).form_valid(form)

class RecipeListView(ListView):
    """ View to list all recipes, with optional meal type filtering, default is set to view all """
    model = Recipe
    template_name = 'recipes/recipe_list.html' 
    context_object_name = 'recipes'

    def get_queryset(self):
        """ Filters recipes by meal type """
        queryset = super().get_queryset()
        meal_type = self.request.GET.get('meal_type')

        if meal_type:
            queryset = queryset.filter(meal_type=meal_type)

        return queryset

    def get_context_data(self, **kwargs):
        """ Adds meal type filter choices to the context """
        context = super().get_context_data(**kwargs)
        meal_type = self.request.GET.get('meal_type')
        context['meal_type'] = meal_type
        context['meal_type_choices'] = Recipe.MEAL_TYPE_CHOICES
        return context

class RecipeDetailView(DetailView):
    """ View to display details of a specific recipe """
    model = Recipe
    template_name = 'recipes/recipe_detail.html'  
    context_object_name = 'recipe'  

@login_required
def profile_view(request):
    """ View to display the logged-in user's profile with their recipes """
    user_recipes = Recipe.objects.filter(author=request.user)  
    return render(request, 'recipes/profile.html', {'user': request.user, 'user_recipes': user_recipes})


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    """ View to update an existing recipe """
    model = Recipe
    template_name = 'recipes/edit_recipe.html'
    fields = ['title', 'description', 'ingredients', 'instructions', 'calories']
    context_object_name = 'recipe'

    def form_valid(self, form):
        """ Displays a success message upon updating the recipe """
        messages.success(self.request, 'Recipe updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        """ Redirects to the recipe detail page after successful update """
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    """ View to delete a recipe and associated reviews """
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    context_object_name = 'recipe'

    def get_success_url(self):
        """ Displays a success message and redirects to the recipe list after deletion """
        messages.success(self.request, 'Recipe deleted successfully!')
        return reverse_lazy('recipe_list')

    def delete(self, request, *args, **kwargs):
        """ Deletes the recipe and its associated reviews """
        self.object = self.get_object()
        self.object.review_set.all().delete()
        self.object.delete()
        return redirect(self.get_success_url())
        
class RateRecipeView(LoginRequiredMixin, View):
    """ View to allow users to rate a recipe """
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