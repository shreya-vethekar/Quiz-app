from django.db import models
from django.db.models.deletion import CASCADE
import uuid

# Create your models here.

#different choices for difficulty level
DIFF_CHOCIES=(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)
class Quiz(models.Model):
    quiz_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    quiz_name=models.CharField(max_length=120)
    number_of_question=models.IntegerField()
    time=models.IntegerField(help_text="Duration of the quiz in minutes")
    required_score_to_pass=models.IntegerField(help_text="Required score in %")
    difficulty=models.CharField(max_length=6,choices=DIFF_CHOCIES)

    def __str__(self):
        return f"{self.quiz_name}"

    def get_questions(self):
        # here we have all the questions for the quiz
        return self.question_set.all()

    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    question_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    question_text =models.CharField(max_length=200)
    quiz_id=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now=True)
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
    created_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Answer : {self.answer_text} ,correct : {self.correct_answer}"

class UserAnswer(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    #user_id=models.ForeignKey(UserOTP,on_delete=CASCADE)
    question_id=models.ForeignKey(Question,on_delete=CASCADE)
    answer_id=models.ForeignKey(Answer,on_delete=CASCADE)
    user_answer=models.CharField(max_length=200)