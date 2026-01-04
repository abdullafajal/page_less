
from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "tags"]
        widgets = {
             "tags": forms.SelectMultiple(attrs={"class": "form-select", "size": "5"}),
             "category": forms.Select(attrs={"class": "form-select"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Write a comment..."}),
        }
