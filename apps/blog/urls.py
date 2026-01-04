
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("<slug:slug>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("<slug:slug>/comment/", CommentCreateView.as_view(), name="post_comment"),
]
