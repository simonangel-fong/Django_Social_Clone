from django.forms.models import ModelForm
from .models import Blog, Hashtag
from django.forms import CheckboxSelectMultiple


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content", "hashtag")
        widgets = {
            "hashtag": CheckboxSelectMultiple()
        }


class HashtagForm(ModelForm):
    class Meta:
        model = Hashtag
        fields = ("name",)      # must end with comma
