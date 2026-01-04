
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "bio")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    pass
