from django.urls import path
from .views import *
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)


app_name = 'Accounts'

urlpatterns = [
    path('user/signup',UserSignUpView.as_view(),name='user-signup'),
    path('teacher/signup',TeacherCreateView.as_view(),name='teacher-signup'),
    path('student/signup', StudentCreateView.as_view(),name='student-signup'),
    path('user/dashboard',Dashboard.as_view(),name='user-dashboard'),


    path('user/login/',LoginView.as_view(template_name='Accounts/login.html'),name='login'),
    path('user/logout/',LogoutView.as_view(),name='logout')
]