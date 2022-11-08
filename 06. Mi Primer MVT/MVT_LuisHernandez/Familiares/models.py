from django.db import models

# Create your models here.
class Familiar1(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    ID = models.IntegerField()
    fechaNacimiento = models.DateField()
    email = models.EmailField(max_length=40)
    apodo = models.CharField(max_length=20,blank = True)
    profesion = models.CharField(max_length=40)

class Familiar2(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    ID = models.IntegerField()
    fechaNacimiento = models.DateField()
    email = models.EmailField(max_length=40)
    profesion = models.CharField(max_length=40)
    apodo = models.CharField(max_length=40,blank = True)

class Familiar3(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    ID = models.IntegerField()
    fechaNacimiento = models.DateField()
    email = models.EmailField(max_length=40)
    profesion = models.CharField(max_length=40)
    apodo = models.CharField(max_length=40,blank = True)