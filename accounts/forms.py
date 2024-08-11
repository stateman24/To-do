from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1",)

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exist:
            return forms.ValidationError("Email already used")
        return data



