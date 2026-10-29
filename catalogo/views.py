from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def catalogo(request):
    return render(request, 'catalogo/catalogo.html')

def iniciar_sesion(request):

    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request, 
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        
    return render(request, 'catalogo/login.html')
