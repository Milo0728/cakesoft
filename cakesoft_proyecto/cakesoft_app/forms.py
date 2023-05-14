from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm



from django import forms
from django.forms.widgets import DateInput

class RegistroForm(forms.Form):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('P', 'Pasaporte'),
    ]
    
    tipo_documento = forms.ChoiceField(choices=TIPO_DOCUMENTO_CHOICES, label='Tipo Documento')
    id = forms.CharField(max_length=100, label='ID')
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    correo = forms.EmailField(label='Correo')
    numero = forms.CharField(max_length=100, label='Teléfono')
    direccion = forms.CharField(max_length=100, label='Dirección')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=DateInput(attrs={'type': 'date'}))

    def clean_id(self):
        id = self.cleaned_data['id']
        # Realiza cualquier validación adicional que desees para el campo 'id'
        return id

    def save(self):
        id = self.cleaned_data['id']
        tipo_documento = self.cleaned_data['tipo_documento']
        nombre = self.cleaned_data['nombre']
        apellido = self.cleaned_data['apellido']
        correo = self.cleaned_data['correo']
        numero = self.cleaned_data['numero']
        direccion = self.cleaned_data['direccion']
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        
        cliente = Cliente(
            id=id,
            tipo_documento=tipo_documento,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            numero=numero,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento
        )
        
        cliente.save()
        # Realiza cualquier otra acción necesaria después de guardar los datos
        
        return cliente

    
class LoginForm(forms.Form):
    id = forms.CharField(label='Cédula', max_length=10)