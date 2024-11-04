from django.urls import path
from .views import (AddRecipe, RecipeListView,
                    RecipeDetailView, profile_view,
                    RecipeUpdateView, RecipeDeleteView, RateRecipeView)

urlpatterns = [
    path('', AddRecipe.as_view(), name="add_recipe"),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/',
         RecipeDetailView.as_view(), name='recipe_detail'),
    path('profile/', profile_view, name='profile'),
    path('recipes/<int:pk>/edit/',
         RecipeUpdateView.as_view(), name='edit_recipe'),
    path('recipes/<int:pk>/delete/',
         RecipeDeleteView.as_view(), name='delete_recipe'),
    path('rate/<int:recipe_id>/',
         RateRecipeView.as_view(), name='rate_recipe'),
]
