from django.contrib import admin
from .models import *
# Register your models here.


class QuizInline(admin.StackedInline):
    model = Quiz
    extra = 2


@admin.register(QuizSet)
class QuizSetAdmin(admin.ModelAdmin):

    date_hierarchy = 'pub_date'
    list_display = ('name','subject','isPublished')
    inlines = [QuizInline,]
    fieldsets = (
        ('Information' , {'fields' : ('name','subject','isPublished','cover_image_url','desc')}),
        ('Credentials' , {'fields' : ('max_marks_per_quiz',)}),
    )


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):

    date_hierarchy = 'pub_date'
    list_display = ('name','full_marks','allotted_time_in_minutes','isActive')
    inlines = [QuestionInline,]
    fieldsets = (
        ('Quizset' , {'fields' : ('quizset',)}),
        ('Information' , {'fields' : (('name','isActive') , 'syllabus','cover_image_url')}),
        ('Credentials' , {'fields' : (('full_marks','allotted_time_in_minutes','negative_marking'),)}),
    )


class OptionInline(admin.TabularInline):
    model = Option
    extra = 2



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline,]
    fieldsets = (
        ('Quiz' , {'fields' : ('quiz',)}),
        ('Info' , {'fields' :('question_text' , 'marks')}),
    )