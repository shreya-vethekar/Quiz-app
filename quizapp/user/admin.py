from django.contrib import admin
from django.contrib.auth.models import User

from user.models import UserOTP

# Register your models here.
admin.site.register(UserOTP)