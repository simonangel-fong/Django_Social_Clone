from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import BlogForm, HashtagForm
from .models import Blog, Hashtag

from django.contrib.auth import get_user_model

# region public view


class PublicBlogListView(ListView):
    ''' View of blog list '''
    model = Blog
    extra_context = {"title": "Blog List", "heading": "Blog List"}
    template_name = "AppBlog/blog_list.html"

    def get_queryset(self):
        querySet = super().get_queryset()
        querySet = querySet.filter(published_time__isnull=False)
        return querySet


class PublicBlogDetailView(DetailView):
    ''' View of blog detail '''
    model = Blog
    extra_context = {"title": "Blog Detail", "heading": "Blog Detail"}
    template_name = "AppBlog/blog_detail.html"


class HashtagListView(ListView):
    model = Hashtag
    extra_context = {"title": "All Hashtag", "heading": "All Hashtag"}
    template_name = "AppBlog/hashtag_list.html"

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


class HashtagCreateView(LoginRequiredMixin, CreateView):
    model = Hashtag
    form_class = HashtagForm
    extra_context = {"title": "Hashtag New", "heading": "Hashtag New"}
    template_name = "AppBlog/hashtag_form.html"

    # customizes process when form is valid.
    def form_valid(self, form):
        self.object = form.save(commit=False)   # gets the object from the form
        # assigns the request user to user field
        self.object.name = self.object.name.strip()  # strip the hashtag name
        self.object.save()                      # saves the Blog object
        return super().form_valid(form)         # calls the parent form_valid()


def hashtagDetail(request, slug):
    ''' public view for each hashtag '''
    hashtag = get_object_or_404(Hashtag, slug=slug)

    context = {
        "title": f"Hashtag:{hashtag.name}",
        "heading": f"Hashtag:{hashtag.name}",
        # find blogs with hashtag
        "blog_list": Blog.objects.filter(hashtag=hashtag, published_time__isnull=False)
    }
    print(context)
    template = "AppBlog/hashtag_detail.html"
    return render(request, template, context)


# endregion
