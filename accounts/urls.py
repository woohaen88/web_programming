from django.urls import path

from accounts import views

app_name = "accounts"

urlpatterns = [
    # account/signup
    path("signup/", views.AccountSignUpView.as_view(), name="signup"),
    path("signin/", views.AccountSignInView.as_view(), name="signin"),
    path("signout/", views.AccoutSignoutView.as_view(), name="signout"),
]
