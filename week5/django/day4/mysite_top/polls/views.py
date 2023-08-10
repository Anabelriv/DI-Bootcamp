from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author


# Create your views here.
def index(request):
    message = "Hello this is my first page"
    return HttpResponse(message)


def post(request, post_id: int):
    data = {1: "This is the 1st post", 2: "This is the 2nd post"}

    post = data.get(post_id, "No such post")
    return HttpResponse(post)


def about(request):
    text = "<h1>This is my first frontend project<\h1>\n" * 100

    return HttpResponse(text)


def all_posts(request, author_name):
    try:
        author_instance = Author.objects.get(name=author_name)
        author_posts = Post.objects.filter(author=author_instance)
        formatted_posts = "\n".join(post.title for post in author_posts)
        return HttpResponse(formatted_posts)
    except Author.DoesNotExist:
        return HttpResponse(f"No posts found for author {author_name}")
