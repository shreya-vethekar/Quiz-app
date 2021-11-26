from django.contrib import admin
from .models import Quiz
from .models import UserAnswer
from .models import Question,Answer
# Register your models here.
admin.site.register(Quiz)
admin.site.register(UserAnswer)
class AnswerInline(admin.TabularInline):
    model=Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
