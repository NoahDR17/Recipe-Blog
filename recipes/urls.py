from django.urls import path
from .views import AddRecipe, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', AddRecipe.as_view(), name="add_recipe"),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),

]
