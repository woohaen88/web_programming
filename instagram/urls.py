from django.urls import path
from django.views.generic import TemplateView
from instagram import views


app_name = "instagram"
urlpatterns = [
    path("", TemplateView.as_view(template_name="instagram/layout.html"), name="index"),
    path("create/", views.InstagramPostCreateView.as_view(), name="post_create"),
    path("<int:post_pk>/", views.InstagramDetailView.as_view(), name="post_detail"),
]
