from django.views.generic import CreateView, ListView, DetailView
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
