from django.shortcuts import render,redirect
from AuthApp.decorator import check_session_key,check_student_session,check_teacher_session
from django.views.decorators.cache import never_cache
from AuthApp.models import CustomUser
from .forms import AddCouseForm
from django.contrib import messages
from .models import Courses



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
    

