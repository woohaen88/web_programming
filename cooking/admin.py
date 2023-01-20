from django.contrib import admin
from .models import Food, Recipe, Ingredient


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
