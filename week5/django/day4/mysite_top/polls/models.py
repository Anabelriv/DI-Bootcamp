from typing import Collection, Optional
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
    # category_set/categories (ManytoMany with Category)


# author model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)  # by default null, values ar not allowed
    email = models.EmailField(blank=True, null=True)


class Profile(models.Model):
    author = models.OneToOneField("Author", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)
    # profile onetoone with profile model
    # post_set(one to many with the post model)


class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField("Post", related_name="categories")

    # conspiracy

    def clean(self):  # clean _<field_name> usage in forms
        if "conspiracy" == self.name:
            raise ValidationError(f"Can't have conspiracy in category name")
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# blank don't have to provide value for the field


# migration - instruction for the db about changes (adding a table, changing a column etc.)

# py manage.py makemigrations
# py manage.py migrate
