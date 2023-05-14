from imaplib import _Authenticator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.contrib.auth.views import LoginView as BaseLoginView

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import authenticate, login, logout

from .forms import RegistroForm, LoginForm
 
from .models import Categoria, Cliente, Producto

from django.urls import reverse
 
from django.contrib import messages 
 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms

import logging

from django.contrib.auth import login


class Administrar(ListView):
    model = Producto

class RegistroUsuario(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'home/register/index.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'home/register/index.html', {'form': form})

class LoginView(View):
    template_name = 'home/login/index.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            id = form.cleaned_data['id']
            
            try:
                cliente = Cliente.objects.get(id=id)
            except Cliente.DoesNotExist:
                cliente = None
            
            if cliente is not None:
                user = self.authenticate_user(request, cliente)
                if user is not None:
                    login(request, user)
                    request.session['logged_in'] = {'id': cliente.id, 'nombre': cliente.nombre}  # Guardar ID y nombre del cliente en la sesión

                    if cliente.rol == 'admin':
                        return redirect('administrar')  # Redirigir al panel de administración
                    else:
                        return redirect('verProductos')  # Redirigir a la página de productos
        
        # Autenticación fallida, mostrar formulario con mensaje de error
        messages.error(request, 'Credenciales inválidas. Intente nuevamente.')
        return render(request, self.template_name, {'form': form})
    
    def authenticate_user(self, request, cliente):
        user = cliente  # Utilizamos el objeto Cliente como el usuario autenticado
        return user

    
# Productos

class VerProductos(ListView):
    model = Producto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context
    
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')  # Redirige a la página principal o a la URL que desees después del cierre de sesión
    
class ProductoListado(ListView):
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 

class ProductoCrear(SuccessMessageMixin, CreateView):
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py'
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Productos' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente!' # Mostramos este Mensaje luego de Crear un Postre
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
        
# Redireccionamos a la página principal luego de crear un registro o Producto    
    def get_success_url(self):
        return reverse('leerProducto') # Redireccionamos a la vista principal 'leer'

class ProductoDetalle(DetailView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 


class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Producto # Llamamos a la clase 'Producto' que se encuentra en nuestro archivo 'models.py' 
    form = Producto # Definimos nuestro formulario con el nombre de la clase o modelo 'Producto' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Productos' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
    
    # Redireccionamos a la página principal luego de actualizar un registro o Producto
    def get_success_url(self):               
        return reverse('leerProducto') # Redireccionamos a la vista principal 'leer'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o Producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una Producto 
        messages.success (self.request, (success_message))       
        return reverse('leerProducto') # Redireccionamos a la vista principal 'leer'

# Categorias

class CategoriaListado(ListView):
    model = Categoria # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py' 

class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py'
    form = Categoria # Definimos nuestro formulario con el nombre de la clase o modelo 'Categoria'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Categorias' de nuestra Base de Datos 
    success_message = 'Categoria Creado Correctamente!' # Mostramos este Mensaje luego de Crear un Postre
        
# Redireccionamos a la página principal luego de crear un registro o Categoria    
    def get_success_url(self):
        return reverse('leerCategoria') # Redireccionamos a la vista principal 'leer'

class CategoriaDetalle(DetailView): 
    model = Categoria # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py' 


class CategoriaActualizar(SuccessMessageMixin, UpdateView): 
    model = Categoria # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py' 
    form = Categoria # Definimos nuestro formulario con el nombre de la clase o modelo 'Categoria' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Categorias' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Categoria 
    
    # Redireccionamos a la página principal luego de actualizar un registro o Categoria
    def get_success_url(self):               
        return reverse('leerCategoria') # Redireccionamos a la vista principal 'leer'

class CategoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoria 
    form = Categoria
    fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o Categoria
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una Categoria 
        messages.success (self.request, (success_message))       
        return reverse('leerCategoria') # Redireccionamos a la vista principal 'leer'
    
# Clientes

class ClienteListado(ListView):
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py' 


class ClienteDetalle(DetailView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py' 


class ClienteActualizar(SuccessMessageMixin, UpdateView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py' 
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Clientes' de nuestra Base de Datos 
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 
    
    # Redireccionamos a la página principal luego de actualizar un registro o Cliente
    def get_success_url(self):               
        return reverse('leerCliente') # Redireccionamos a la vista principal 'leer'

class ClienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Cliente 
    form = RegistroForm()
    fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o Producto
    def get_success_url(self): 
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una Producto 
        messages.success (self.request, (success_message))       
        return reverse('leerCliente') # Redireccionamos a la vista principal 'leer'