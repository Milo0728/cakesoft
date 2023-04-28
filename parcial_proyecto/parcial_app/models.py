from django.db import models

# Create your models here.

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)

    class Meta:
        db_table = 'equipos'

class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'jugadores'