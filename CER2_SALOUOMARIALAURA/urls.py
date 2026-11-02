"""
URL configuration for CER2_SALOUOMARIALAURA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalogo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('categorias/', views.categorias, name='categorias'),
    path('login/', views.iniciar_sesion, name='login'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('crear_lugar/', views.crear_lugar, name='crear_lugar'),
    path('detalles/<int:id>/', views.detalles, name='detalles'),
]
