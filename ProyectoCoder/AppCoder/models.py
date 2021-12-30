from django.db import models

from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields.files import ImageField

# Create your models here.

class Posteo(models.Model):

    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=80)
    cuerpo = models.TextField()
    imagen = models.ImageField()

    def __str__(self):
        
        return f"TITULO: {self.titulo} SUBTITULO: {self.subtitulo} CUERPO: {self.cuerpo} "



class Usuario(models.Model):
    
    
    apellido = models.CharField(max_length=40)
    nombre = models.IntegerField()
    dni = models.BigIntegerField()
    fecha_nacimiento = models.DateField()
    e_mail = models.EmailField()
    domicilio = models.CharField(max_length=40)
    #id = {lambda x += dni} ---> validar como hacer la función lambda que sume un incremental al id + dni del user. 

    def __str__(self):
        
        return f"APELLIDO: {self.apellido} NOMBRE: {self.nombre} DNI: {self.dni} NACIMIENTO: {self.fecha_nacimiento} EMAIL: {self.e_mail} DOMICILIO: {self.domicilio}"


class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    esNoche = models.BooleanField(null=True)
    
    def __str__(self):
        
        return f"CURSO: {self.nombre} CAMADA: {self.camada} NOCHE: {self.esNoche}"
    
   
    
class Jugador(models.Model):
    
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
    
   
    
    def __str__(self):
        
        return f"{self.apellido}, {self.numero} , {self.esBueno}"
    
    
class Equipo(models.Model):
    
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    
    
class Estadio(models.Model):
    
    direccion = models.CharField(max_length=40)
    anioFund = models.IntegerField()
    
    

class Empleado(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    profesional = models.BooleanField()
    fechaDeNacimiento = models.DateField()
    
    def __str__(self):
        return f"NOMBRE y APELLIDO: {self.nombre} {self.apellido}  ---- DNI: {self.dni}"



class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)