from django.urls import path
from .views import SignupView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = "AppAccount"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(
        template_name="AppAccount/login.html",
        extra_context={"title": "Login", "heading": "Login"}
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", login_required(TemplateView.as_view(
        template_name="AppAccount/profile.html",
        extra_context={"title": "User Profile", "heading": "User Profile"}
    )), name="profile"),
]
