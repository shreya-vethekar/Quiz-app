from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class UserLog(models.Model):
    user_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.username}"

