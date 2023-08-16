from django.contrib import admin
from .models import Blog, Hashtag
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    fields = ("title", "author", "content",)
    list_display = ("title", "author", "created_time", "published_time")
    list_editable = ("author",)
    list_filter = ("author",)
    search_fields = ("title", "content",)


admin.site.site_title = "Blog Admin"
admin.site.site_header = "Blog Admin"
admin.site.register(Blog, BlogAdmin)
admin.site.register(Hashtag)
