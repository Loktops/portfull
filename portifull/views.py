from django.shortcuts import render
from django import http
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Cria as views( logica do site )
def sing(request): 
    if request.method == 'GET':
        return render(request, 'sing.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verifica se o usuário já existe
        user = User.objects.filter(username=username).first()
        if user:
            return http.HttpResponse('Usuario já existe')
        
        # Verifica se o email já está cadastrado
        email_exists = User.objects.filter(email=email).first()
        if email_exists:
            return http.HttpResponse('Email já cadastrado')
        
        # Cria o usuáriouser 
        User.objects.create_user(username=username, email=email, password=password)
        User.save()
        return http.HttpResponse('Usuario criado com sucesso')

def logon(request):
    if request.method == 'GET':
        return render(request, 'logon.html')
    else:
        # Processa o login
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
        else:
            return http.HttpResponse('Usuario ou senha incorretos')

@login_required
def home(request):
    if  User.is_authenticated:
        return render(request, 'home.html')
    else:
        return http.HttpResponse('Você não está logado')
    
def logout_view(request):
    logout(request)
    return redirect('logon')