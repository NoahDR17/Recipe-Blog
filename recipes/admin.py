from django.contrib import admin
from .models import Recipe, Review, Rating

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Rating)


