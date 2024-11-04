from django import forms
from .models import Recipe, Review


class RecipeForm(forms.ModelForm):
    """ The Form to Create a Recipe """
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "instructions",
            "ingredients",
            "meal_type",
            "calories",
        ]
    labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "meal_type": "Meal Type",
            "calories": "Calories",
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating']
