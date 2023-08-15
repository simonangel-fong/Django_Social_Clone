from django.views.generic import ListView
from AppBlog.models import Blog


class HomeView(ListView):
    ''' Home page '''
    model = Blog
    extra_context = {"title": "Home", "heading": "Home"}
    template_name = "index.html"
