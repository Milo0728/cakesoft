"""
URL configuration for cakesoft_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path

from cakesoft_app.views import LoginView, Administrar, RegistroUsuario, CustomLogoutView
from cakesoft_app.views import VerProductos, ProductoListado, ProductoDetalle, ProductoCrear, ProductoActualizar, ProductoEliminar
from cakesoft_app.views import CategoriaActualizar, CategoriaCrear, CategoriaDetalle, CategoriaEliminar, CategoriaListado
from cakesoft_app.views import ClienteActualizar, ClienteDetalle, ClienteEliminar, ClienteListado

urlpatterns = [
    
    path('admins/', admin.site.urls),
    #  La ruta 'leer' en donde listamos todos los registros o productos de la Base de Datos
    path('productos/', VerProductos.as_view(template_name = "home/productos/index.html"), name='verProductos'),
    
    path('', ProductoListado.as_view(template_name = "home/inicio/index.html"), name='inicio'),
    
    path('login/', LoginView.as_view(), name='login'),
    
    path('registro/', RegistroUsuario.as_view(), name='register'),
 
    path('administrar/', Administrar.as_view(template_name = "administrar/index.html"), name='administrar'),
 
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # -- Productos --
    
    # La ruta 'leer' en donde listamos todos los registros o Equipos de la Base de Datos
    path('administrar/producto/', ProductoListado.as_view(template_name = "administrar/producto/index.html"), name='leerProducto'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un productos o registro 
    path('administrar/producto/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "administrar/producto/detalles.html"), name='detalleProducto'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo productos o registro  
    path('administrar/producto/crear', ProductoCrear.as_view(template_name = "administrar/producto/crear.html"), name='crearProducto'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un productos o registro de la Base de Datos 
    path('administrar/producto/editar/<int:pk>', ProductoActualizar.as_view(template_name = "administrar/producto/actualizar.html"), name='actualizarProducto'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un productos o registro de la Base de Datos 
    path('administrar/producto/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminarProducto'),   
    
    # -- Categorias --
    
    # La ruta 'leer' en donde listamos todos los registros o Equipos de la Base de Datos
    path('administrar/categoria/', CategoriaListado.as_view(template_name = "administrar/categoria/index.html"), name='leerCategoria'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categorias o registro  
    path('administrar/categoria/crear', CategoriaCrear.as_view(template_name = "administrar/categoria/crear.html"), name='crearCategoria'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Categorias o registro de la Base de Datos 
    path('administrar/categoria/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "administrar/categoria/actualizar.html"), name='actualizarCategoria'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categorias o registro de la Base de Datos 
    path('administrar/categoria/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='eliminarCategoria'),   
    
    # -- Clientes --
    
     # La ruta 'leer' en donde listamos todos los registros o Equipos de la Base de Datos
    path('administrar/cliente/', ClienteListado.as_view(template_name = "administrar/cliente/index.html"), name='leerCliente'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Clientes o registro 
    path('administrar/cliente/detalle/<int:pk>', ClienteDetalle.as_view(template_name = "administrar/cliente/detalles.html"), name='detalleCliente'),
    
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Clientes o registro de la Base de Datos 
    path('administrar/cliente/editar/<int:pk>', ClienteActualizar.as_view(template_name = "administrar/cliente/actualizar.html"), name='actualizarCliente'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Clientes o registro de la Base de Datos 
    path('administrar/cliente/eliminar/<int:pk>', ClienteEliminar.as_view(), name='eliminarCliente'),   
]

