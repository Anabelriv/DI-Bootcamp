from django.db import models
from django.contrib.auth.models import User

type = [("sun", "sunny"), ("wd", "windy"), ("rn", "rainy"), ("st", "stormy")]


# Create your models here.
class Report(models.Model):
    forecaster = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=type)

    # last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.id}"
