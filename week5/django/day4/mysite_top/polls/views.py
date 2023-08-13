from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author, Category


# Create your views here.
def index(request):
    message = "Hello this is my first page"
    return HttpResponse(message)


def post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        content = f"AUTHOR:{post.author}| TITLE: {post.title}|Text:{post.text}"
        return HttpResponse(post, content)
    except Post.DoesNotExist:
        return HttpResponse("No such post")


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


def category_posts(request, category_id: int):
    try:
        category_instance = Category.objects.get(id=category_id)
        category_posts = category_instance.posts.all()
        formatted_posts = "\n".join(post.title for post in category_posts)
        return HttpResponse(formatted_posts)
    except Category.DoesNotExist:
        return HttpResponse(f"No posts found for category {category_id}")
