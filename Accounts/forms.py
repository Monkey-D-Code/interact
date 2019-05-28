from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=130)
    last_name = forms.CharField(max_length=130)
    email = forms.EmailField(max_length=254)
    

    class Meta:
        model = User
        fields = ('first_name' , 'last_name' , 'username' , 'email' , 'password1' , 'password2')
        widgets = {
            'password1': forms.PasswordInput() ,
            'password2' : forms.PasswordInput() ,
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_', ' ').capitalize()
            })

    

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_', ' ').capitalize()
            })


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_', ' ').capitalize()
            })
    
