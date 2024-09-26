from django.urls import path
from . import views

urlpatterns = [
    path("student_home", views.StudentHome, name="student_home"),
    path("show_quiz/<str:course_id>", views.ShowQuiz, name="show_quiz"),
    path("student_profile", views.StudentProfile, name="student_profile"),
    path("show_courses", views.CourseDetails, name="show_courses"),
    
    
]
