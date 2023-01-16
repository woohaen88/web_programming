from django.urls import path

from accounts import views

app_name = "accounts"

# rest framework
from rest_framework import routers
from accounts import apis

router = routers.DefaultRouter()
router.register(r"user", apis.UserViewSet)

urlpatterns = [
    # account/signup
    path("signup/", views.AccountSignUpView.as_view(), name="signup"),
    path("signin/", views.AccountSignInView.as_view(), name="signin"),
    path("signout/", views.AccoutSignoutView.as_view(), name="signout"),
]
