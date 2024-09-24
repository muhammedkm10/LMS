
from django.urls import path
from . import views

urlpatterns = [
    path("teacher_home",views.TeacherHome,name='teacher_home'),
    path("add_course",views.AddCourse,name='add_course'),
    path('edit_course/<str:id>/', views.EditCourse, name='edit_course'),
    path('delete_course/<str:id>/', views.DeleteCourse, name='delete_course'),
    path('add_quiz/<str:code>/<str:course_id>/', views.AddQuiz, name='add_quiz'),
    path('show_quiz/<str:course_id>', views.ShowQuiz, name='show_quiz'),
    path('delete_quiz/<str:course_id>', views.DeleteQuiz, name='delete_quiz'),
    
    
    
    

    
    
]

