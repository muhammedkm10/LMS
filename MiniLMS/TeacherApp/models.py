from django.db import models
from AuthApp.models import CustomUser

# Create your models here.

class Courses(models.Model):
    teacher = models.ForeignKey(CustomUser,related_name="teacher", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50,null=True)
    description  = models.TextField(null=True)
    quiz_added  = models.BooleanField(default=False)
    
