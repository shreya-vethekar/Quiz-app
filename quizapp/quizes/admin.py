from django.contrib import admin
from django.db.models.query_utils import Q
from .models import Quiz
# Register your models here.
admin.site.register(Quiz)