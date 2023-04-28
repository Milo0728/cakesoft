"""parcial_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from parcial_app.views import EquipoListado, EquipoDetalle, EquipoCrear, EquipoActualizar, EquipoEliminar, JugadorListado, JugadorDetalle, JugadorCrear, JugadorActualizar, JugadorEliminar

urlpatterns = [
    path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todos los registros o Equipos de la Base de Datos
    path('equipos/', EquipoListado.as_view(template_name = "equipos/index.html"), name='leerEquipo'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Equipos o registro 
    path('equipos/detalle/<int:pk>', EquipoDetalle.as_view(template_name = "equipos/detalles.html"), name='detallesEquipo'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Equipos o registro  
    path('equipos/crear', EquipoCrear.as_view(template_name = "equipos/crear.html"), name='crearEquipo'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Equipos o registro de la Base de Datos 
    path('equipos/editar/<int:pk>', EquipoActualizar.as_view(template_name = "equipos/actualizar.html"), name='actualizarEquipo'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Equipos o registro de la Base de Datos 
    path('equipos/eliminar/<int:pk>', EquipoEliminar.as_view(), name='eliminarEquipo'),   
    
    
    # JUGADORES
    
    # La ruta 'leer' en donde listamos todos los registros o Equipos de la Base de Datos
    path('jugadores/', JugadorListado.as_view(template_name = "jugadores/index.html"), name='leerJugador'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Jugadors o registro 
    path('jugadores/detalle/<int:pk>', JugadorDetalle.as_view(template_name = "jugadores/detalles.html"), name='detallesJugador'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Jugadors o registro  
    path('jugadores/crear', JugadorCrear.as_view(template_name = "jugadores/crear.html"), name='crearJugador'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Jugadors o registro de la Base de Datos 
    path('jugadores/editar/<int:pk>', JugadorActualizar.as_view(template_name = "jugadores/actualizar.html"), name='actualizarJugador'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Jugadors o registro de la Base de Datos 
    path('jugadores/eliminar/<int:pk>', JugadorEliminar.as_view(), name='eliminarJugador'),   
]
