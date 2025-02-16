from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MinValueValidator


class Recipe(models.Model):
    """
    The model to create recipes
    """
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
    ]

    title = models.CharField(max_length=250, blank=False,
                             null=False,  unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_author")
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = models.CharField(max_length=10000, null=False, blank=False)
    instructions = models.CharField(max_length=10000, null=False, blank=False)
    calories = models.IntegerField(validators=[MinValueValidator(0)])
    created_on = models.DateTimeField(auto_now_add=True)
    meal_type = models.CharField(max_length=10,
                                 choices=MEAL_TYPE_CHOICES,
                                 default='breakfast')

    def average_rating(self):
        reviews = Review.objects.filter(recipe=self)
        if reviews.exists():
            return reviews.aggregate(Avg('rating'))['rating__avg']
        return 0

    def delete(self, *args, **kwargs):
        # Delete all related reviews before deleting the recipe
        self.review_set.all().delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent multiple reviews from the same user
        unique_together = ('user', 'recipe')
