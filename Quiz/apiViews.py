from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Question , 
    Quiz,
)
from .serializers import (
    QuestionSerializer,
    QuizSerializer,
)

from django.shortcuts import get_object_or_404

class QuestionsListView(ListAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.queryset.filter(quiz_id=self.kwargs.get('pk'))


class QuizRetrieveView(RetrieveAPIView):
    queryset = Quiz.objects.filter(isActive=True)
    serializer_class = QuizSerializer

    def get_object(self):
        return get_object_or_404(
            self.queryset,
            id = self.kwargs.get('pk')
        )


class ProcessResultView(APIView):

    def post(self, request):
        AnswerSheet = request.data
        print(AnswerSheet)
        return Response(str(AnswerSheet))