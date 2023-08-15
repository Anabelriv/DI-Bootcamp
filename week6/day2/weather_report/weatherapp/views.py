from django.shortcuts import render
from .serializers import ReportSerializer
from .models import Report
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsForecaster


class ReportView(APIView):
    permission_classes = [IsForecaster, IsAuthenticated]

    def get(self, request, *args, **kwargs):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer = ReportSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)

        self.check_object_permissions(request, report)
        report.delete()
        return Response({"message": f"Report id - {pk} DELETED"})

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
