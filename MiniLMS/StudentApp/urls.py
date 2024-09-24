
from django.urls import path
from . import views

urlpatterns = [
    path("student_home",views.StudentHome,name='student_home'),
    
]
