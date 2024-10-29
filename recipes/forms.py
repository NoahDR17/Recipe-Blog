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
            "calories",
        ]
    
    labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "calories": "Calories",
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating']