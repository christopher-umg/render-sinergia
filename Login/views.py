
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate




# Create your views here.
def helloWorld(request):
    return render(request,'index.html')

def LoginPage(request):
    if request.method == 'GET':
        return render(request,'Pages/Login.html')
    else:
        user = authenticate(request,username=request.POST['userName'],password=request.POST['password'])
        if user is None:
            return render(request,'Pages/Login.html',{
                'error': 'usuario o contraseña es incorrecto'
            })
        else:
            login(request,user)
            return redirect('home_page')

def homePage(request):
    return render(request,'Pages/home.html')

def SingUpPage(request):
    if request.method =='GET':
        return render(request,'Pages/SignUp.html')
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['Username'],password=request.POST['password1'],email=request.POST['Correo'])
                user.save()
                return redirect('login_page')
            except:
                return render(request, 'Pages/SignUp.html',{
                    "error": "Usuario existente en la BDD"
                })
        return render(request,'Pages/SignUp.html',{
            "error": "Contraseñas no coinciden"
        })

def projectPage(request):
    return render(request,'Pages/Proyectos.html')

def jobsPage(request):
    return render(request,'Pages/BolsaTrabajo.html')

def helpPage(request):
    return render(request,'Pages/espacioApoyo.html')

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')