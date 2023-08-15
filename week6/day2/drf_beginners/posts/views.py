from django.shortcuts import render
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django.http import JsonResponse

from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from .permissions import ISAuthenticatedAndAdmin


class PostView(APIView):
    permission_classes = [IsAuthenticated, ISAuthenticatedAndAdmin]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response({"message": f"Post id - {pk} DELETED"})


@csrf_exempt
def post_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        serializer = PostSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({"error": "Invalid json data"})
