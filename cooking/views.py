from django.shortcuts import render
from django.views.generic import ListView

from .models import Food, Recipe, Ingredient


def index(request):
    return render(request, "cooking/index.html")


class CookingListView(ListView):
    model = Food
    context_object_name = "food_list"
    template_name = "cooking/index.html"
