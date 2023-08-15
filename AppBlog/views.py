from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import BlogForm
from .models import Blog

from django.contrib.auth import get_user_model

# region public view


class PublicBlogListView(ListView):
    ''' View of blog list '''
    model = Blog
    extra_context = {"title": "Blog List", "heading": "Blog List"}
    template_name = "AppBlog/blog_list.html"


class PublicBlogDetailView(DetailView):
    ''' View of blog detail '''
    model = Blog
    extra_context = {"title": "Blog Detail", "heading": "Blog Detail"}
    template_name = "AppBlog/blog_detail.html"


# endregion

# region Author view

def authorBlogPanelView(request):
    ''' panel view of blog '''
    context = {
        "title": "Blog Panel",
        "heading": "Blog Panel",
        "blog_list": Blog.objects.filter(
            author=request.user,
            published_time__isnull=False
        ),
        "draft_list": Blog.objects.filter(
            author=request.user,
            published_time__isnull=True
        )
    }
    template = "AppBlog/blog_panel.html"
    return render(request, template, context)


def authorBlogPublishView(request, pk):
    ''' publish blog '''
    blog = get_object_or_404(Blog, pk=pk)
    blog.publish()
    return redirect("AppBlog:panel")


class AuthorBlogCreateView(LoginRequiredMixin, CreateView):
    ''' Blog create for author '''
    model = Blog
    form_class = BlogForm
    extra_context = {"title": "Blog New", "heading": "Blog New"}
    template_name = "AppBlog/blog_form.html"

    # customizes process when form is valid.
    def form_valid(self, form):
        print(self.request.user.username)
        self.object = form.save(commit=False)   # gets the object from the form
        print("request", self.request)
        print("type", type(self.request.user))
        print(get_user_model())
        # assigns the request user to user field
        self.object.author = self.request.user
        self.object.save()                      # saves the Blog object
        return super().form_valid(form)         # calls the parent form_valid()


class AuthorBlogUpdateView(LoginRequiredMixin, UpdateView):
    ''' Blog update for author '''
    model = Blog
    form_class = BlogForm
    extra_context = {"title": "Blog Edit", "heading": "Blog Edit"}
    template_name = "AppBlog/blog_form.html"


class AuthorBlogDeleteView(LoginRequiredMixin, DeleteView):
    ''' Blog delete for author '''
    model = Blog
    extra_context = {"title": "Blog Delete", "heading": "Blog Delete"}
    success_url = reverse_lazy("AppBlog:list")

# endregion
