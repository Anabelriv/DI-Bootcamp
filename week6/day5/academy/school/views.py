from django.shortcuts import render
from rest_framework.response import Response
from django.views import View
from .models import Course, Teacher
from rest_framework import status
from .serializers import TeacherSerializer
from rest_framework.views import APIView


class CourseDetailsView(View):
    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            data = {
                "course_name": course.course_name,
                "course_code": course.course_code,
            }
            return Response(data)
        except Course.DoesNotExist:
            return Response("error")


class TeacherAPIView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
