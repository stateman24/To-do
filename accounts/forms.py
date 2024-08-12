from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "username",
            "class": "username",
            "placeholder": "Your username goes here"
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "first-name",
            "class": "firstname",
            "placeholder": "Your name goes here"
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "email-address",
            "class": "email",
            "placeholder": "Your email goes here",
            "required": True
        },
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "id": "password",
            "class": "pass",
            "placeholder": "Your password goes here"
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "id": "password2",
            "class": "pass2",
            "placeholder": "Confirm your password"
        }
    ))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password2"] != cd["password1"]:
            return forms.ValidationError("Password Mismatch")
        return cd["password2"]

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            return forms.ValidationError("Email already used")
        return data


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "id": "username",
            "class": "username",
            "placeholder": "Your Username"
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "id": "password",
            "class": "password",
            "placeholder": "Your Password"
        }
    ))
