from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)


# author model
class Author(models.Model):
    name = models.CharField(max_length=50)  # by default null, values ar not allowed
    email = models.EmailField(blank=True, null=True)


# blank don't have to provide value for the field


# migration - instruction for the db about changes (adding a table, changing a column etc.)

# py manage.py makemigrations
# py manage.py migrate
