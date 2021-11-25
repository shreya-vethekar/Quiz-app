from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from user.views import login
@login_required(login_url=reverse_lazy("login"))
def home(request):
    return render(request,"quizes/home.html")


