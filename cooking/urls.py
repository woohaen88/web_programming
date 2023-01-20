from django.urls import path

from .views import index
from . import views

app_name = "cooking"

urlpatterns = [
    path("", views.CookingListView.as_view(), name="index"),
]