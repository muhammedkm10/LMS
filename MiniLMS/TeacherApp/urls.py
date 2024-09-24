
from django.urls import path
from . import views

urlpatterns = [
    path("teacher_home",views.TeacherHome,name='teacher_home'),
    path("add_course",views.AddCourse,name='add_course'),
    path('edit_course/<str:id>/', views.EditCourse, name='edit_course'),

    
    
]

