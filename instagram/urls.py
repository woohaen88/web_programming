from django.urls import path
from django.views.generic import TemplateView
from instagram import views
from django.contrib.auth.validators import UnicodeUsernameValidator


app_name = "instagram"
urlpatterns = [
    path("create/", views.InstagramPostCreateView.as_view(), name="post_create"),
    path("<int:post_pk>/", views.InstagramDetailView.as_view(), name="post_detail"),
    path("<username>/", views.UserPage.as_view(), name="user_page"),
    path("<username>/follow/", views.UserFollowView.as_view(), name="user_follow"),
    # path("<username>/follow/", views.user_follow, name="user_follow"),
    path(
        "<username>/unfollow/", views.UserUnFollowView.as_view(), name="user_unfollow"
    ),
    path("", views.InstagramIndexView.as_view(), name="index"),
]
