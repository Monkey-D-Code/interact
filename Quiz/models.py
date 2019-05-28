from django.db import models

# Create your models here.
class QuizSet(models.Model):

    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    isPublished = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add = True)
    cover_image_url = models.URLField(max_length=300)
    max_marks_per_quiz = models.IntegerField()
    desc = models.TextField()
    


    def __str__(self):
        return self.name


class Quiz(models.Model):

    quizset = models.ForeignKey(QuizSet , on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    syllabus = models.TextField()

    
    allotted_time_in_minutes = models.IntegerField()
    negative_marking = models.BooleanField(default=False)
    cover_image_url = models.URLField(max_length=300)

    isActive = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quizzes'

    def full_marks(self):
        marks = False
        for question in self.question_set.all():
            marks += question.marks
        return marks


class Question(models.Model):

    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)
    question_text = models.TextField()
    
    pub_date = models.DateField(auto_now_add=True)
    pub_time = models.TimeField(auto_now_add=True)

    
    marks = models.IntegerField()

    def __str__(self):
        return self.question_text

    

    @property
    def options(self):
        return self.option_set.all()

        
class Option(models.Model):

    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    option_text = models.TextField()
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text


