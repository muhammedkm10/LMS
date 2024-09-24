from django.shortcuts import render,redirect,get_object_or_404
from AuthApp.decorator import check_session_key,check_student_session,check_teacher_session
from django.views.decorators.cache import never_cache
from AuthApp.models import CustomUser
from .forms import AddCouseForm,EditCouseForm
from django.contrib import messages
from .models import Courses,Quiz
import requests




# teacher home
@check_session_key('email')
@check_teacher_session
@never_cache
def TeacherHome(request):
    email = request.session["email"]
    current_user = CustomUser.objects.get(email = email)
    courses_queryset = Courses.objects.filter(teacher = current_user)
    
    context = {
        "courses_queryset":courses_queryset,
        'username':current_user.username
    }
    return render(request,"TeacherHome.html",context)



# add course function for teachers

def AddCourse(request):
    print('i am working yoo')
    if request.method == "POST":
        form = AddCouseForm(data=request.POST)
        email = request.session["email"]
        current_user = CustomUser.objects.get(email = email)
        choices = {
            "9":"General knowledge",
            "21":"Sports",
            "28":"Vehicles",
            "22":"Geography",
            "27":"Animals"
        }
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            Courses.objects.create(teacher = current_user,name=choices[name],code=name,description=description) 
            messages.success(request,'Your course added succesfully..')
            return redirect("teacher_home")
        else:
            print(form.errors)
            messages.error(request,"Select name or The  description should contain 10 letters")
            return redirect("teacher_home")
    



# edit course function
def EditCourse(request,id):
    print(id)
    if request.method == "POST":
        form = EditCouseForm(data=request.POST)
        email = request.session["email"]
        current_user = CustomUser.objects.get(email = email)
        choices = {
            "9":"General knowledge",
            "21":"Sports",
            "28":"Vehicles",
            "22":"Geography",
            "27":"Animals"
        }
        if form.is_valid():
            description = form.cleaned_data['description']
            Courses.objects.filter(id=id).update(teacher = current_user,description=description) 
            messages.success(request,'Your course updated succesfully..')
            return redirect("teacher_home")
        else:
            print(form.errors)
            messages.error(request,"Select name or The  description should contain 10 letters")
            return redirect("teacher_home")
    
    
# Delete course
def DeleteCourse(request,id):
      course = Courses.objects.get(id = id)
      Quiz.objects.filter(course= course).delete()
      course.delete()
      messages.success(request,'Your course deleted succesfully..')
      return redirect("teacher_home")
      
      
# add quiz for a particular course
def AddQuiz(request,code,course_id):
    url = f"https://opentdb.com/api.php?amount=10&category={code}&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        api_response = response.json()
        course = Courses.objects.get(id=course_id)  # Fetch the course object

        for item in api_response['results']:
            Quiz.objects.create(
                course=course,
                question=item['question'],
                correct_answer=item['correct_answer'],
                incorrect_answers=item['incorrect_answers']  # This will be stored as a list in JSONField
            )
        course.quiz_added = True
        course.save()
        messages.success(request,'Quiz added for the course succesfully...')
        return redirect("teacher_home") 
    else:
        messages.error(request,"Some error occured ,Retry after some time...")
        return redirect("teacher_home") 
        
    
    
# show quiz
def ShowQuiz(request,course_id):
    course = get_object_or_404(Courses, id=course_id)  # Fetch the specific course
    quizzes = Quiz.objects.filter(course=course)  # Get all quizzes for this course
    
    context = {
        'course': course,
        'quizzes': quizzes,
    }
    return render(request,"ShowQuizToTeacher.html",context)

# delete quiz
def DeleteQuiz(request,course_id):
    course = Courses.objects.get(id = course_id)
    Quiz.objects.filter(course= course).delete()
    course.quiz_added = False
    course.save()
    messages.success(request,'Quiz deleted succesfully...')
    return redirect("teacher_home") 

        
    


