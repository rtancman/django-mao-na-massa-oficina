from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import OrdemServico


def index(request):
    return render(request, 'core/home.html', {})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()

    return render(request, 'core/login.html', {'form_login': form_login})

def orderm_servico(request):
    if not request.user.is_authenticated:
        return redirect('/entrar')

    ordens_servico = OrdemServico.objects.filter(carro__usuario=request.user).order_by('data_criacao')
    return render(request, 'core/ordem_servico.html', {'ordens_servico': ordens_servico})

def logout(request):
    auth_logout(request)
    return redirect('/')