from django.shortcuts import render
from AuthApp.decorator import check_session_key,check_student_session,check_teacher_session
from django.views.decorators.cache import never_cache


# student home
@check_session_key('email')
@check_student_session
@never_cache
def StudentHome(request):
    return render(request,"StudentHome.html")