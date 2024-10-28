from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    """
    The model to create recipes
    """
    title = models.CharField(max_length=250, blank=False, null=False,  unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_author")
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = models.CharField(max_length=10000, null=False, blank=False)
    instructions = models.CharField(max_length=10000, null=False, blank=False)
    calories = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
