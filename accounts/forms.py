import random
import string

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


def get_random_strings(length):
    gen_str = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
    gen_idx = random.choice(string.ascii_uppercase)
    return f"{gen_idx}/{gen_str}"


class AccountSignUpForm(UserCreationForm):
    # email = forms.EmailField(
    #     required=True,
    #     widget=forms.EmailInput(
    #         attrs={
    #             # "class": "form-control form-control-lg",
    #             "type": "email",
    #             "id": "email",
    #         }
    #     ),
    # )
    #
    # password1 = forms.CharField(
    #     required=True,
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "type": "password",
    #             "id": "password",
    #             # "class": "form-control form-control-lg",
    #         }
    #     ),
    # )
    #
    # password2 = forms.CharField(
    #     required=True,
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "type": "password",
    #             "id": "password-confirm",
    #             # "class": "form-control form-control-lg",
    #         }
    #     ),
    # )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)

        not_exist = True
        while not_exist:
            username = get_random_strings(8)
            get_user = self.Meta.model.objects.filter(username=username)
            if not get_user.exists():
                user.username = username
                not_exist = False
        user.save()
        return user


class AccountSignInForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "email",
                "id": "email",
            }
        ),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "id": "password",
                "class": "form-control form-control-lg",
            }
        ),
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("email이 존재하지 않습니다.")
        return email

    def clean(self):
        email = self.clean_email()
        password = self.cleaned_data.get("password")
        user = User.objects.filter(email=email)
        if user.exists():
            if user.first().check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is Wrong"))
        else:
            self.add_error("email", forms.ValidationError("해당 유저는 존재하지 않습니다."))
