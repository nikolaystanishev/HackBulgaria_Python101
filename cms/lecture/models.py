from django.db import models
from course.models import Course


# Create your models here.
class Lecture(models.Model):
    name = models.CharField(max_length=50)
    week = models.IntegerField()
    course = models.ForeignKey(Course)
    url = models.CharField(max_length=100)
