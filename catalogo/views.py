from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import LugarPatrimonial, Categoria

# Create your views here.

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def catalogo(request):
    lugares = LugarPatrimonial.objects.all()
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')

    if categoria_id:
        lugares = lugares.filter(categoria_id=categoria_id)

    return render(request, 'catalogo/catalogo.html', {'lugares':lugares, 'categorias': categorias})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/categorias.html', {'categorias': categorias})

def detalles(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)

    if request.method == 'POST':

        if not request.user.has_perm('catalogo.change_lugarpatrimonial'):
            return redirect('catalogo')

        lugar.nombre = request.POST.get('nombre')
        lugar.descripcion = request.POST.get('descripcion')
        lugar.ubicacion = request.POST.get('ubicacion')
        lugar.anio_construccion = request.POST.get('anio_construccion')
        lugar.imagen = request.POST.get('imagen')

        lugar.save()

        return redirect('detalles', id=lugar.id)

    return render(request, 'catalogo/detalles.html', {
        'lugar': lugar
    })

def iniciar_sesion(request):

    if request.method == 'POST':
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

def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)

    return redirect('inicio')

@login_required(login_url='login')
@permission_required('catalogo.add_categoria', raise_exception=True)
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.POST.get('imagen')

        Categoria.objects.create(
            nombre = nombre,
            descripcion = descripcion,
            imagen = imagen
        )

        return redirect('catalogo') 

    return render(request, 'catalogo/crear_categoria.html')

@login_required(login_url='login')
@permission_required('catalogo.add_lugarpatrimonial', raise_exception=True)
def crear_lugar(request):

    categorias = Categoria.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        ubicacion = request.POST.get('ubicacion')
        anio = request.POST.get('anio')
        imagen = request.POST.get('imagen')
        categoria_id = request.POST.get('categoria')

        categoria = Categoria.objects.get(id=categoria_id)

        LugarPatrimonial.objects.create(
            nombre = nombre,
            descripcion = descripcion,
            ubicacion = ubicacion,
            anio = anio,
            imagen = imagen,
            categoria = categoria
        )

        return redirect('catalogo')

    return render(request, 'catalogo/crear_lugar.html', {
        'categorias': categorias})
