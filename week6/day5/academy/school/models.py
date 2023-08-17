from django.db import models

# Create your models here.

from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)

    def __str__(self):
        return self.course_name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
