from django.urls import path
from .views import (
    authorBlogPanelView, authorBlogPublishView,
    PublicBlogListView, PublicBlogDetailView,
    AuthorBlogCreateView, AuthorBlogUpdateView, AuthorBlogDeleteView
)

# namesapce for this app's urls
app_name = "AppBlog"

urlpatterns = [
    # public views
    path("list/", PublicBlogListView.as_view(), name="public_list"),
    path("detail/<int:pk>", PublicBlogDetailView.as_view(), name="detail"),

    # author views, cud
    path("author/panel", view=authorBlogPanelView, name="panel"),
    path("author/publish/<int:pk>", view=authorBlogPublishView, name="publish"),
    path("author/new/", AuthorBlogCreateView.as_view(), name="create"),
    path("author/edit/<int:pk>", AuthorBlogUpdateView.as_view(), name="update"),
    path("author/delete/<int:pk>", AuthorBlogDeleteView.as_view(), name="delete"),
]
