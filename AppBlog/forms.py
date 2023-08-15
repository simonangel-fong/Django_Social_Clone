from django.forms.models import ModelForm
from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content")
