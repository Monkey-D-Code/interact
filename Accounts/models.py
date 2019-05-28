from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Student(models.Model):

    gender_choices = (
        ('M' , 'Male'),
        ('F' , 'Female'),
        ('O' , 'Others'),
    )

    user = models.OneToOneField(User , on_delete = models.CASCADE)
    middle_name = models.CharField(blank=True , max_length=50)
    date_of_birth = models.DateField(help_text="Should be in 'YYYY-MM-DD' format")
    gender = models.CharField(choices=gender_choices , max_length=50)
    contact_number = models.DecimalField(max_digits =10 , decimal_places=0)
    address = models.TextField()
    display_picture = models.URLField(max_length=400 , blank=True)
    name_of_father = models.CharField(blank=True , max_length=200)
    name_of_mother = models.CharField(blank=True , max_length=200)

    def full_name(self):
        return str(self.user.first_name)+" "+str(self.middle_name)+" "+str(self.user.last_name)

    def __str__(self):
        return self.full_name()

    def age(self):
        today = date.today() 
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)) 
        return age 




class Teacher(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=150,blank=True)
    date_of_birth = models.DateField(help_text="'YYYY-MM-DD' format")
    specialised_subject = models.TextField()
    previous_work_expreience = models.TextField()
    working_as = models.TextField()
    display_picture = models.URLField(blank=True,max_length=400)
    joining_date = models.DateField(auto_now_add=True)
    joining_time = models.TimeField(auto_now_add=True)

    contact_number = models.DecimalField(max_digits=10 , decimal_places=0)
    alternate_number = models.DecimalField(max_digits=10 , decimal_places=0 ,  blank=True)

    address = models.TextField()

    def full_name(self):
        return str(self.user.first_name)+" "+str(self.middle_name)+" "+str(self.user.last_name)

    def __str__(self):
        return self.full_name()

    def age(self):
        today = date.today() 
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)) 
        return age 

