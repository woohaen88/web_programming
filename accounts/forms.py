import random
import string

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


def get_random_strings(length):
    gen_str = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
    return f"{gen_str}"


class AccountSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")


class AccountSignInForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
            }
        ),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
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
