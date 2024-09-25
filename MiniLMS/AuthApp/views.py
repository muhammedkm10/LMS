from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from .models import CustomUser, TeacherDetails
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.


# landing page view function
@never_cache
def LandingPage(request):
    if "email" in request.session:
        if request.session["role"] == "student":
            return redirect("student_home")
        else:
            return redirect("teacher_home")
    return render(request, "Landing.html")


# signup functions for both students and teachers
@never_cache
def UserSignup(request):
    if "email" in request.session:
        if request.session["role"] == "student":
            return redirect("student_home")
        else:
            return redirect("teacher_home")

    # for form submissions
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        role = request.POST.get("role")
        # if the data is valid saving to the db
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = CustomUser.objects.create_user(
                username=username, email=email, password=password, role=role
            )
            login(request, user)
            # Customize session data
            request.session["email"] = email
            request.session["role"] = role
            # Save the session
            request.session.save()
            if role == "student":
                return redirect("student_home")
            else:
                qualification = request.POST.get("qualification")

                TeacherDetails.objects.create(teacher=user, education=qualification)
                return redirect("teacher_home")
        else:
            # if  form validation failed
            messages.error(request, "Enter valid credentials...")
            if role == "student":
                return render(request, "StudentSignup.html")
            else:
                return render(request, "TeacherSignup.html")
    # for initial rendering of the pages
    role = request.GET.get("role")
    if role == "teacher":
        return render(request, "TeacherSignup.html")
    elif role == "student":
        return render(request, "StudentSignup.html")


# login functions for both students and teachers
@never_cache
def UserLogin(request):
    if "email" in request.session:
        if request.session["role"] == "student":
            return redirect("student_home")
        elif request.session["role"] == "teacher":
            return redirect("teacher_home")
    # for form submissions
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")
        # Authenticate the user
        user = authenticate(email=email, password=password)
        if user and user.role != role:
            if role == "student":
                messages.error(request, "Enter valid credential for student")
                return render(request, "StudentLogin.html")
            else:
                messages.error(request, "Enter valid credential for teacher")
                return render(request, "TeacherLogin.html")
        if user is not None:
            # Check if the user is a student
            login(request, user)
            # Customize session data
            request.session["email"] = email
            request.session["role"] = role
            # Save the session
            request.session.save()
            if role == "student":
                return redirect("student_home")
            return redirect("teacher_home")
        else:
            messages.error(request, "Enter valid email and password")
            if role == "student":
                return render(request, "StudentLogin.html")
            else:
                return render(request, "TeacherLogin.html")
    # for initial rendering of the pages
    role = request.GET.get("role")
    if role == "teacher":
        return render(request, "TeacherLogin.html")
    elif role == "student":
        return render(request, "StudentLogin.html")
    return render(request, "StudentLogin.html")


# logout function
def Logout(request):
    request.session.clear()
    # Log out the user
    logout(request)
    return redirect("landing")


@never_cache
def NotFound(request):
    return render(request, "NotFound.html")
