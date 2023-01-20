from django.db import models
from django.conf import settings


class Food(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 내용
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="images/food/thumbnail/%Y/%m/%d")

    # foreign_key
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipes"
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="recipe")
    step = models.PositiveIntegerField()
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to=f"images/recipe/%Y/%m/%d/", blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recipe::{self.food.name}"


class Ingredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="ingredient")
    material = models.CharField(max_length=10)
    amount = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ingredient::{self.food.name}"
