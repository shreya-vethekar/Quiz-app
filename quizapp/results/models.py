from django.db import models
from django.db.models.deletion import CASCADE
from quizes.models import Quiz
from questions.models import Question,Answer
#from user.models import UserOTP
import uuid
# Create your models here.
class UserAnswer(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    #user_id=models.ForeignKey(UserOTP,on_delete=CASCADE)
    question_id=models.ForeignKey(Question,on_delete=CASCADE)
    answer_id=models.ForeignKey(Answer,on_delete=CASCADE)
    user_answer=models.CharField(max_length=200)