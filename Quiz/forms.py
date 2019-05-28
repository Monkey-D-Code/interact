from django import forms
from .models import *

class QuizsetForm(forms.ModelForm):

    class Meta:
        model = QuizSet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_', ' ').capitalize()+" of category"
            })



class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        exclude = ('quizset',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_', ' ').capitalize()+" of category"
            })



class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = ("quiz",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_', ' ').capitalize()+" of category"
            })


class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        exclude = ("question",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_', ' ').capitalize()+" of category"
            })

        