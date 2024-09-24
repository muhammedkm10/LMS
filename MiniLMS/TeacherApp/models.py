from django.db import models
from AuthApp.models import CustomUser

# Create your models here.


# model for the courses
class Courses(models.Model):
    teacher = models.ForeignKey(CustomUser,related_name="teacher", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50,null=True)
    description  = models.TextField(null=True)
    quiz_added  = models.BooleanField(default=False)
    
    
    
# model for the quiz

class Quiz(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE) 
    question = models.TextField(null=True)
    correct_answer = models.CharField(max_length=255,null=True)
    incorrect_answers = models.JSONField(null=True)  

    def __str__(self):
        return self.question
    

    
