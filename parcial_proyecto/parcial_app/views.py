from django.shortcuts import render

# Create your views here.
 
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Equipo' para poder usarlo en nuestras Vistas CRUD
from .models import Equipo, Jugador

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class EquipoListado(ListView):
    model = Equipo # Llamamos a la clase 'Equipo' que se encuentra en nuestro archivo 'models.py' 

class EquipoCrear(SuccessMessageMixin, CreateView):
    model = Equipo # Llamamos a la clase 'Equipo' que se encuentra en nuestro archivo 'models.py'
    form = Equipo # Definimos nuestro formulario con el nombre de la clase o modelo 'Equipo'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Equipos' de nuestra Base de Datos 
    success_message = 'Equipo Creado Correctamente!' # Mostramos este Mensaje luego de Crear un Postre
        
# Redireccionamos a la página principal luego de crear un registro o Equipo    
    def get_success_url(self):
        return reverse('leerEquipo') # Redireccionamos a la vista principal 'leer'

class EquipoDetalle(DetailView): 
    model = Equipo # Llamamos a la clase 'Equipo' que se encuentra en nuestro archivo 'models.py' 


class EquipoActualizar(SuccessMessageMixin, UpdateView): 
    model = Equipo # Llamamos a la clase 'Equipo' que se encuentra en nuestro archivo 'models.py' 
    form = Equipo # Definimos nuestro formulario con el nombre de la clase o modelo 'Equipo' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Equipos' de nuestra Base de Datos 
    success_message = 'Equipo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Equipo 
    
    # Redireccionamos a la página principal luego de actualizar un registro o Equipo
    def get_success_url(self):               
        return reverse('leerEquipo') # Redireccionamos a la vista principal 'leer'

class EquipoEliminar(SuccessMessageMixin, DeleteView): 
    model = Equipo 
    form = Equipo
    fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o Equipo
    def get_success_url(self): 
        success_message = 'Equipo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una Equipo 
        messages.success (self.request, (success_message))       
        return reverse('leerEquipo') # Redireccionamos a la vista principal 'leer'
    
# Jugadores    
    
class JugadorListado(ListView):
    model = Jugador # Llamamos a la clase 'Jugador' que se encuentra en nuestro archivo 'models.py' 

class JugadorCrear(SuccessMessageMixin, CreateView):
    model = Jugador # Llamamos a la clase 'Jugador' que se encuentra en nuestro archivo 'models.py'
    form = Jugador # Definimos nuestro formulario con el nombre de la clase o modelo 'Jugador'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Jugadors' de nuestra Base de Datos 
    success_message = 'Jugador Creado Correctamente!' # Mostramos este Mensaje luego de Crear un Postre
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipos'] = Equipo.objects.all()
        return context
    
    # Redireccionamos a la página principal luego de crear un registro o Jugador    
    def get_success_url(self):
        return reverse('leerJugador') # Redireccionamos a la vista principal 'leer'

class JugadorDetalle(DetailView): 
    model = Jugador # Llamamos a la clase 'Jugador' que se encuentra en nuestro archivo 'models.py' 


class JugadorActualizar(SuccessMessageMixin, UpdateView): 
    model = Jugador # Llamamos a la clase 'Jugador' que se encuentra en nuestro archivo 'models.py' 
    form = Jugador # Definimos nuestro formulario con el nombre de la clase o modelo 'Jugador' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Jugadors' de nuestra Base de Datos 
    success_message = 'Jugador Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Jugador 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipos'] = Equipo.objects.all()
        return context
    
    # Redireccionamos a la página principal luego de actualizar un registro o Jugador
    def get_success_url(self):               
        return reverse('leerJugador') # Redireccionamos a la vista principal 'leer'

class JugadorEliminar(SuccessMessageMixin, DeleteView): 
    model = Jugador 
    form = Jugador
    fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o Jugador
    def get_success_url(self): 
        success_message = 'Jugador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una Jugador 
        messages.success (self.request, (success_message))       
        return reverse('leerJugador') # Redireccionamos a la vista principal 'leer'