from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

#Formulaire de connexion
def login_user(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username,password=pwd)
            if user is not None:
                login(request, user) #variante de connexion-déconnexion, stock l'utilisateur dans l'objet request
                return redirect('home')
            else:
                messages.error(request, "Authentification échouée")
                return render(request,'login.html',{'form':form})
        else:       
            return render(request,'login.html',{'form':form})          
    else:
        form = LoginForm()            
        return render(request,'login.html',{'form':form})

def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']      
            email = form.cleaned_data['email']   
            pwd = form.cleaned_data['pwd']   
            user = User.objects.create_user(username = username,  email = email, password = pwd)
            if user is not None:
                return redirect('login-user')
            else:
                messages.error(request,'Création échouée, veuillez réessayer.')
                return render(request,'register.html',{'form':form})
        else:
            return render(request,'register.html',{'form':form})       

    form = RegisterForm()
    return render(request,'register.html',{'form':form})   

def logout_user(request):
    logout(request)
    return render(request, 'index.html')     

def procedure(request):
    return render(request,'procedure.html')    