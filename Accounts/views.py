from django.views.generic import (
    FormView,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import *
from .models import *

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.





class UserSignUpView(FormView):

    form_class = UserCreationForm
    template_name = 'Accounts/User/create.html'
    success_url = reverse_lazy('Quiz:exam')
        
    



class TeacherCreateView(CreateView):

    form_class = TeacherForm
    template_name = 'Accounts/Teacher/create.html'


class StudentCreateView(CreateView):

    form_class = StudentForm
    template_name = 'Accounts/Student/create.html'


class Dashboard(TemplateView):

    template_name = 'Accounts/dashboard.html'
