from django.contrib import admin
from recipes.models import Ingredient
from recipes.models import Recipe

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
