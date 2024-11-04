from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student_tbl(models.Model):
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.student_name}  {self.email}"
