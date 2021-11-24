from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.urls.base import reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth.models import User
from .models import UserOTP
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import pyotp 



def index(request):
    return render(request,"user/index.html")

def register(request):
    form=CreateUserForm()

    if request.method =="POST":
        get_otp=request.POST.get('otp')
        if get_otp:
           get_user=request.POST.get('user')
           user=User.objects.get(username=get_user)
           if get_otp ==UserOTP.objects.filter(user=user).last().otp:
               user.is_active=True
               user.save()
               messages.success(request,f"Your Account has been created {user.username}")
               return redirect('login')
           else:
                messages.error(request,f"You entered a wrong OTP")
                return render(request,"user/register.html",{'otp':True,'user':user}) 



        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            base32 = pyotp.random_base32()
            totp = pyotp.TOTP(base32)
            otp = totp.now()
            user=User.objects.get(username=username)
            user.is_active=False
            user_otp = otp 
            user.save()
            #form.save() 
            #user_otp=random.randint(100000,999999)
            UserOTP.objects.create(user=user,otp=user_otp)
            #message of mail
            message_mail=f"Hello {username},\n Your OTP is {user_otp} \n Thank you"
            send_mail(
                "Welcome !! -Verify your Email",
                message_mail,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
                )
            
            return render(request,"user/register.html",{'otp':True,'user':user})
       

    else:
        form=CreateUserForm()
        #messages.error(request,f"Account not created")
     

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
            return redirect("home")
        else:
            messages.error(request,f"Account Do not exit please sign in")
    form=AuthenticationForm()
    return render(request,"user/login.html")


@login_required(login_url=reverse_lazy("login"))
def home(request):
    return render(request,"quizes/home.html")
    
def password_reset(request):
    return render(request,'password_reset.html')

def password_reset_done(request):
    return render(request,"password_reset_done.html")
 
def password_reset_complete(request):
    return render(request,"password_reset_complete.html")