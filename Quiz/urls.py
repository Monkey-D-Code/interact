from django.urls import path
from .views import *
from .apiViews import (
    QuestionsListView,
    QuizRetrieveView,
    ProcessResultView,
)

app_name = 'Quiz'

urlpatterns = [
    path('exam/',Exam.as_view(),name='exam'),
    path('home/',HomeView.as_view(),name='home'),
    path('quizset/<int:pk>/details',QuizSetDetailView.as_view(),name='quizset-details'),
    path('<int:pk>/take-the-quiz/',TakeQuizView.as_view(),name='take-quiz'),
    path('<int:pk>/start/',QuizView.as_view(),name='start-quiz'),


    path('<int:pk>/questions/' , QuestionsListView.as_view(),name='questions-list'),
    path('<int:pk>/details/',QuizRetrieveView.as_view(),name='quiz-details'),
    path('process-result/',ProcessResultView.as_view(),name='result'),
]
