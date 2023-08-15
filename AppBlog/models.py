from django.db import models
from django.urls import reverse
from AppAccount.models import UserAccount
from django.contrib.auth import get_user_model
from django.utils import timezone
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("AppBlog:detail", kwargs={"pk": self.pk})

    def publish(self, *args, **kwargs):
        self.published_time = timezone.now()
        self.save()

    class Meta:
        ordering = ["-last_modified_time",]
