from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Employee, Project, Task
from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    ProjectSerializer,
    TaskSerializer,
)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDepartmentAdmin

# Create your views here.


class DepartmentAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDepartmentAdmin]

    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                department = Department.objects.get(id=id)
                serializer = DepartmentSerializer(department)

            except Department.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(instance=department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        department = Department.objects.get(id=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDepartmentAdmin]

    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                employee = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(employee)

            except Employee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            employees = Employee.objects.all()
            serializer = DepartmentSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDepartmentAdmin]

    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                project = Project.objects.get(id=id)
                serializer = EmployeeSerializer(project)

            except Project.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            projects = Project.objects.all()
            serializer = DepartmentSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(instance=project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDepartmentAdmin]

    def get(self, request, **kwargs):
        id = kwargs.get("pk", None)
        if id is not None:
            try:
                task = Task.objects.get(id=id)
                serializer = TaskSerializer(task)

            except Department.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
