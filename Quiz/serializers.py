from rest_framework.serializers import ( 
    ModelSerializer,
    Serializer,
    DecimalField,
)
from .models import *


class QuizSerializer(ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'




class OptionSerializer(ModelSerializer):

    class Meta:
        model = Option
        fields = ('option_text',)

class QuestionSerializer(ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id','question_text' , 'pub_date' , 'pub_time' , 'marks' , 'options')




