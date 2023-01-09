from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from accounts.forms import AccountSignUpForm, AccountSignInForm


class AccountSignUpView(CreateView):
    template_name = "accounts/account-signup.html"
    form_class = AccountSignUpForm
    model = get_user_model()
    success_url = reverse_lazy("index")


class AccountSignInView(FormView):
    template_name = "accounts/account-signin.html"
    form_class = AccountSignInForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        valid = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = get_user_model().objects.filter(email=email).first()
        login(self.request, user)
        return valid

    def get_success_url(self):
        return reverse("index")


class AccoutSignoutView(LogoutView):
    pass
