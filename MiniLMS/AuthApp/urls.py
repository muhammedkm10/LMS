
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.LandingPage,name='landing'),
    path("signup",views.UserSignup,name='signup'),
    path("login",views.UserLogin,name='login'),
    path("logout",views.Logout,name='logout'),
    path("not_found",views.NotFound,name="not_found")
    
    
    
    
]
