from django.shortcuts import render
from students.serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here


class Student_listView(APIView):
    # permission_classes = (AllowAny, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        date_joined_param = request.GET.get("date_joined")

        if date_joined_param:
            # Extract the date part from the datetime string
            date_joined = date_joined_param.split("T")[0]
            students = Student.objects.filter(date_joined=date_joined)
        else:
            students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Student_detailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
