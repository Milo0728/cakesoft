from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'categorias'

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

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=254)
    numero_de_telefono = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'clientes'

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
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
