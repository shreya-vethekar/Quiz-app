from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class UserOTP(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    time_stamp=models.DateTimeField(auto_now=True)
    otp=models.SmallIntegerField()



