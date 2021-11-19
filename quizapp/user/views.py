
from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import CreateUserForm

def index(request):
    return render(request,"user/index.html")

def register(request):
    form=CreateUserForm()

    if request.method =="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            messages.success(request,f"Your Account has been created !")
            return redirect('login')

    else:
        form=CreateUserForm()
        messages.info(request,f"account not created")
     

    context={'form':form}
    return render(request,"user/register.html",context)

def Login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            form=login(request,user)
            messages.success(request,f"Welcome {username} !!")
            return redirect('index')
        else:
            messages.info(request,f"Account Do not exit please sign in")
    form=AuthenticationForm()
    return render(request,"user/login.html")
    
# Create your views here.
