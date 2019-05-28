from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .forms import *
from .models import *

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(TemplateView):

    template_name = 'Quiz/home.html'

class Exam(LoginRequiredMixin ,TemplateView):

    template_name = 'Quiz/exam.html'
    login_url = reverse_lazy('Accounts:login')

    def get_context_data(self, **kwargs):
        context = super(Exam, self).get_context_data(**kwargs)
        context['quizsets'] = QuizSet.objects.filter(isPublished=True)
        return context


class QuizSetDetailView(LoginRequiredMixin, DetailView):

    queryset = QuizSet.objects.filter(isPublished=True)
    template_name = 'Quiz/QuizSet/details.html'
    login_url = reverse_lazy('Accounts:login')


class TakeQuizView(LoginRequiredMixin ,DetailView):

    queryset = Quiz.objects.filter(isActive=True)
    template_name = 'Quiz/TakeQuiz/detail.html'
    login_url = reverse_lazy('Accounts:login')


class QuizView(LoginRequiredMixin ,TemplateView):

    template_name = 'Quiz/TakeQuiz/start.html'
    login_url = reverse_lazy('Accounts:login')
    
    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        context['quiz'] = Quiz.objects.get(pk=self.kwargs.get('pk'))
        return context