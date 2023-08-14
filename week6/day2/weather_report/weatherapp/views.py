from django.shortcuts import render
from .serializers import ReportSerializer
from .models import Report
from rest_framework.response import Response
from rest_framework.views import APIView


class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)


# @csrf_exempt
# def post_view(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     if request.method == "POST":
#         serializer = PostSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         else:
#             return JsonResponse({"error": "Invalid json data"})
