from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    descreption = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
