from django.shortcuts import render

# Create your views here.
def login(request):
    return render (request,"login.html",{})

def register(request):
    return render (request,"register.html",{})

def forgetpass(request):
    return render( request ,"forgetpass.html",{})


def home(request):
    return render(request,"home.html",{})