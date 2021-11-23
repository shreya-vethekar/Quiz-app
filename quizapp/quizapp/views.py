from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def handleLogin(request):
    if request.method =="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(request,username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials ,Please try again")
            return redirect("home")
    return HttpResponse('handleLogin') 

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect("/")
#return HttpResponse('handleLogout') 