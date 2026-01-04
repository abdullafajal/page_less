
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from .models import Post, Category, Tag, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect, get_object_or_404

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().select_related("author", "category").prefetch_related("tags")
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return super().get_queryset().select_related("author", "category").prefetch_related("tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_message = "Post created successfully!"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.object.slug})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_message = "Post updated successfully!"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.object.slug})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        messages.success(self.request, "Post deleted successfully!")
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        post = get_object_or_404(Post, slug=self.kwargs["slug"])
        form.instance.post = post
        form.instance.author = self.request.user
        self.object = form.save()
        messages.success(self.request, "Comment added!")
        return redirect(reverse("blog:post_detail", kwargs={"slug": post.slug}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, slug=self.kwargs["slug"])
        return context

    template_name = "blog/partials/comment_form_only.html"
