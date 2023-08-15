from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify


# get custom user model as User
User = get_user_model()


class Blog(models.Model):
    # the author of current post
    author = models.ForeignKey(
        User,   # refer to a custom user model
        on_delete=models.CASCADE
    )
    # title of current post
    title = models.CharField(max_length=64)
    # content of current post
    content = models.TextField(default="")
    # published time
    published_time = models.DateTimeField(null=True, blank=True)
    # created time,
    created_time = models.DateTimeField(auto_now_add=True)
    # last modified time
    last_modified_time = models.DateTimeField(auto_now=True)
    # hashtag
    hashtag = models.ManyToManyField(
        "AppBlog.Hashtag",
        related_name="blogs",       # the name used to refer to current blog from Hashtag
        related_query_name="blogs",  # the name used to look up filter from Hashtag
        through="BlogHashtag"       # the name of intermediate table
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("AppBlog:detail", kwargs={"pk": self.pk})

    def publish(self, *args, **kwargs):
        self.published_time = timezone.now()
        self.save()

    class Meta:
        ordering = ["-last_modified_time",]


class BlogHashtag(models.Model):
    ''' manual intermediate table  '''

    blog = models.ForeignKey(
        "AppBlog.Blog",
        on_delete=models.CASCADE
    )

    hashtag = models.ForeignKey(
        "AppBlog.Hashtag",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.blog.title

    class Meta:
        unique_together = ("blog", "hashtag")     # unique together


class Hashtag(models.Model):
    # name of hashtag
    name = models.CharField(
        max_length=32,  # less than 32 chars
        unique=True     # must be unique
    )
    slug = models.SlugField(
        unique=True,        # must be unique
        allow_unicode=True,  # accepts Unicode letters
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("AppBlog:hashtag_detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["name"]     # default ordered by name