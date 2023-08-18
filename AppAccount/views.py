from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserSignupForm


class SignupView(CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy("AppAccount:login")
    template_name = "AppAccount/signup.html"
    extra_context = {"title": "Sign up", "heading": "Sign up for free"}
