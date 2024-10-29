from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class AddRecipe(LoginRequiredMixin, CreateView):
    """ Add Recipe View """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    context_object_name = "recipes"
    success_url = '/recipes/recipes/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)

class RecipeListView(ListView):
    """ View to list all recipes """
    model = Recipe
    template_name = 'recipes/recipe_list.html' 
    context_object_name = 'recipes' 

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

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    context_object_name = 'recipe'

    def get_success_url(self):
        return reverse_lazy('recipe_list')