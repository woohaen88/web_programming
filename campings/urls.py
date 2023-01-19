from django.urls import path

from . import views

app_name = "campings"

urlpatterns = [
    path("", views.CampingListView.as_view(), name="index"),
    path("create/", views.CampingCreateView.as_view(), name="create"),
    path("detail/<int:camping_pk>/", views.CampingDetailView.as_view(), name="detail"),
    path("update/<int:camping_pk>/", views.CampingUpdateView.as_view(), name="update"),
    # path("update/<int:camping_pk>/", views.CampingUpdateView, name="update"),
    path(
        "camping_item/", views.CampingItemListView.as_view(), name="camping_item_index"
    ),
    path(
        "camping_item/create",
        views.CampingItemCreateView.as_view(),
        name="camping_item_create",
    ),
]
