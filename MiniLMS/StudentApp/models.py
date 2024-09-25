from django.db import models
from AuthApp.models import CustomUser
from TeacherApp.models import Courses
# Create your models here.

class QuizSubmissionDetails(models.Model):
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='student')
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course')
    score = models.IntegerField(null=True)
    date = models.DateField(null=True)
