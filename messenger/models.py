from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):

    usuario = models.ForeignKey(User,on_delete = models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta():

        ordering = ['fecha_creacion']

class Hilo(models.Model):

    usuarios = models.ManyToManyField(User, related_name='hilos')
    mensajes = models.ManyToManyField(Message)