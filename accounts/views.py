from django.shortcuts import render, redirect
from .forms import SignUpForm


def sign_up(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return redirect("accounts:login")
    else:
        user_form = SignUpForm()
    context = {"user_form": user_form}
    return render(request, "accounts/signup.html", context)
