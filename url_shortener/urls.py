from django.urls import path
from rest_framework import routers

from url_shortener import apis
from url_shortener import views

router = routers.SimpleRouter()
router.register(r"url", apis.UrlViewSet)

app_name = "url_shortener"
urlpatterns = [
    path("create/", views.UrlCreateView.as_view(), name="create"),
    path("update/<url_pk>/", views.UrlUpdateView.as_view(), name="update"),
    path("delete/<url_pk>/", views.UrlDeleteView.as_view(), name="delete"),
    path("", views.UrlListView.as_view(), name="index"),
]
