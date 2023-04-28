from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Cliente, Producto

from django.urls import reverse
 
from django.contrib import messages 
 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms

class ProductoListado(ListView):
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 

class Login(ListView):
    model = Cliente

class ProductoCrear(SuccessMessageMixin, CreateView):
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py'
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Productos' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente!' # Mostramos este Mensaje luego de Crear un Postre
        
# Redireccionamos a la página principal luego de crear un registro o Producto    
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ProductoDetalle(DetailView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 


class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Productos' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
    
    # Redireccionamos a la página principal luego de actualizar un registro o Producto
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o Producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una Producto 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'