from django.shortcuts import render

# Create your views here.
def login(request):
    
    return render (request,"login.html",{})

def doLogin(request):
    email = request.POST ['email']
    password = request.POST ['password'] 
    usrObj = User.objects.filter( email = "hari@gmail.com", password= "ram12").first()
    if usrObj:
        return render(request,"home.html",{})
        
    else:
        return render (request,"login.html",{})
    
def register(request):
    return render (request,"register.html",{})

def forgetpass(request):
    return render( request ,"forgetpass.html",{})


def home(request):
    return render(request,"home.html",{})