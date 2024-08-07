from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Password Change
    path("passwordchange/",
         auth_views.PasswordChangeView.as_view(template_name="accounts/passwordchange.html"),
         name="passwordChange"),
    path("passwordchangedone/",
         auth_views.PasswordChangeDoneView.as_view(template_name="accounts/passwordchangedone.html"),
         name="passwordChangeDone"),

    # Reset Password
]

