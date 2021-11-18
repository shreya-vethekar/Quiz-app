from django.db import models
from django.db.models.deletion import CASCADE
from quizes.models import Quiz
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)   #from quizes model.py
    user=models.ForeignKey(User,on_delete=models.CASCADE)   #from user model.py
    score=models.FloatField()

    def __str__(self):
        return str(self.pk)
