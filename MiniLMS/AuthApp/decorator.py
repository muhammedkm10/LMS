from functools import wraps
from django.shortcuts import redirect


# common session checking decorator
def check_session_key(key):
    def decorator(view_func):
        def wrapper(request):
            if key not in request.session:
                return redirect("login")
            return view_func(request)
        return wrapper
    return decorator


# decorator for techers session (techers only pages)
def check_teacher_session(view_func):
        def wrapper(request):
            if request.session["role"] == "teacher":
                return view_func(request)
            else:
                return redirect("not_found")
        return wrapper


# decorator for student session (students only pages)
def check_student_session(view_func):
        def wrapper(request):
            if request.session["role"] == "student":
                return view_func(request)
            else:
                return redirect("not_found")
        return wrapper
