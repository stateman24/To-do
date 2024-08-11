from django.urls import path
from django.contrib.auth import views as auth_views
from .views import sign_up
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path("signup/", sign_up, name="sign_up"),

    path("login/",
         auth_views.LoginView.as_view(template_name="accounts/login.html", authentication_form=LoginForm),
         name="login"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Password Change
    path("passwordchange/",
         auth_views.PasswordChangeView.as_view(template_name="accounts/passwordchange.html", success_url="password_change_done"),
         name="passwordChange"),
    path("passwordchange/password_change_done/",
         auth_views.PasswordChangeDoneView.as_view(template_name="accounts/passwordchangedone.html"),
         name="password_change_done"),

]
