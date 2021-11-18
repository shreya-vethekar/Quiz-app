from django.db import models
from django.db.models.deletion import CASCADE
from quizes.models import Quiz  # import Quiz model from quizes app
# Create your models here.
class Question(models.Model):
    text =models.CharField(max_length=200)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        #here we haveall answers for the questions
        return self.answer_set.all() # related to model Answer


class Answer(models.Model):
    text=models.CharField(max_length=200)
    correct=models.BooleanField(default=False)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question :{self.question} ,Answer : {self.text} ,correct : {self.correct}"