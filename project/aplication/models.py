from django.db import models


# Create your models here.
class clientes(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=200)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=200)

class prendas(models.Model):
    id_prenda=models.IntegerField(primary_key=True)
    color=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)

class contenedores(models.Model):
    id_conte=models.IntegerField(primary_key=True)
    marca=models.CharField(max_length=50)
    capacidad=models.IntegerField()

class lavadora(models.Model):
    id_lavad=models.IntegerField(primary_key=True)
    marcalav=models.CharField(max_length=50)
    capacidadlav=models.IntegerField()

class secadora(models.Model):
    id_secad=models.IntegerField(primary_key=True)
    marcasec=models.CharField(max_length=50)
    capacidadsec=models.IntegerField()
    