from django.db import models
from quizes.models import Quiz  # import Quiz model from quizes app
import uuid
# Create your models here.
class Question(models.Model):
    question_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    question_text =models.CharField(max_length=200)
    quiz_id=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=200)
    scores=models.FloatField()

    def __str__(self):
        return str(self.question_text)

    def get_answers(self):
        #here we haveall answers for the questions
        return self.answer_set.all() # related to model Answer


class Answer(models.Model):
    answer_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    answer_text=models.CharField(max_length=200)
    correct_answer=models.BooleanField(default=False)
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer : {self.answer_text} ,correct : {self.correct_answer}"