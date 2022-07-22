from email import message
from django.shortcuts import render,  HttpResponse

from django.template import loader 

from .models import *

# Create your views here.
def login(request):
    
    return render (request,"login.html",{})

def doLogin(request):
    email = request.POST['email']
    password = request.POST['password'] 
    usrObj = User.objects.filter( email = email, password= password).first()
    if usrObj:
        return render(request,"home.html",{})
        
    else:
        message = "plz enter correct information"
        return render (request,"login.html",{'msg':message})
    
def register(request):
    return render (request,"register.html",{})

def forgetpass(request):
    return render( request ,"forgetpass.html",{})


def home(request):
    return render(request,"home.html",{})