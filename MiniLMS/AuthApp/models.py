from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True,unique=False)
    email =  models.EmailField(max_length=100, blank=True, null=True,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  
    

    def __str__(self):
        return self.email 
    
    
    
class TeacherDetails(models.Model):
    teacher = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    education = models.CharField(max_length=100,null=True,blank=True)
    
    