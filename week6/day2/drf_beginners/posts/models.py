from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY_CHOICES = [("sci", "scientific"), ("na", "nature")]


class Post(models.Model):
    # author > User
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    # last_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.id}"
