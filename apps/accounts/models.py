
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model for Page_Less.
    """
    bio = models.TextField(blank=True, verbose_name="Bio")
    
    # Add any other custom fields here
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
