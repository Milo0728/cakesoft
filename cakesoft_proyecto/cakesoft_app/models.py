import datetime
from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'categorias'
        
class Cliente(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=10, default='')
    tipo_documento = models.CharField(max_length = 15, null = False, default='')
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    correo = models.EmailField(max_length=255, default='')
    numero = models.CharField(max_length=10, default='')
    rol = models.CharField(max_length = 50, default='usuario')
    direccion = models.CharField(max_length = 225, null = False, default='')
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    last_login = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'clientes'

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.FileField()
    
    class Meta:
        db_table = 'productos'


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'ventas'

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'facturas'
