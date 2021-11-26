from django.shortcuts import render
from django.views.generic import ListView
from .models import Quiz
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from user.views import login_in

#@method_decorator(login_required(login_url='main_view'),name='dispatch')
class QuizListView(ListView):
    model=Quiz
    template_name='quizes/home.html'


def quiz_view(request,quiz_id):
    quiz=Quiz.objects.get(quiz_id=quiz_id)
    return render(request,'quizes/quiz.html',{'obj':quiz}) 