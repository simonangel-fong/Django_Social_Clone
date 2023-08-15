from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, TemplateView
from AppBlog.models import Blog


class HomeView(ListView):
    ''' Home page '''
    model = Blog
    extra_context = {"title": "Home", "heading": "Home"}
    template_name = "index.html"

    def get_queryset(self):
        querySet = super().get_queryset()
        querySet = querySet.filter(published_time__isnull=False)
        return querySet


class TestView(TemplateView):
    extra_context = {"title": "Test", "heading": "Test"}
    template_name = "test.html"
