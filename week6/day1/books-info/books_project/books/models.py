from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)

# from books import Book

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=255, blank=False)
    published_date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    page_count = models.PositiveIntegerField(blank=False)
    categories = models.CharField(max_length=255, blank=False)
    thumbnail_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = models.TextField(
        validators=[MinLengthValidator(10)], blank=False, null=False
    )

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"
