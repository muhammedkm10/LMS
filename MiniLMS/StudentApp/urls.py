from django.urls import path
from . import views

urlpatterns = [
    path("student_home", views.StudentHome, name="student_home"),
    path("show_quiz/<str:course_id>", views.ShowQuiz, name="show_quiz"),
]
