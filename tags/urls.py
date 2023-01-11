from django.urls import path, re_path
from tags import views

app_name = "tags"
urlpatterns = [
    re_path(r"^(?P<tag_slug>[-\w]+)/$", views.TagView.as_view(), name="tag_slug"),
]
