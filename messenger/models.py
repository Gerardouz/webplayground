from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):

    usuario = models.ForeignKey(User,on_delete = models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta():

        ordering = ['fecha_creacion']
class HiloManager(models.Manager):

    def find(self,user1,user2):

        queryset = self.filter(usuarios=user1).filter(usuarios=user2)

        if (len(queryset) > 0):

            return queryset[0]
        return None

    def find_or_create(self,user1,user2):

        thread = self.find(user1,user2)

        if thread is None:

            thread = Hilo.objects.create()

            thread.usuarios.add(user1,user2)

        return thread



class Hilo(models.Model):

    usuarios = models.ManyToManyField(User, related_name='hilos')
    mensajes = models.ManyToManyField(Message)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    objects = HiloManager()

    class Meta():
        ordering = ['-fecha_actualizacion']

def messages_changed(sender, **kwargs):

    instance= kwargs.pop("instance",None)
    action= kwargs.pop("action",None)
    pk_set= kwargs.pop("pk_set",None)


    print(instance,action,pk_set)
    false_pk_set = set()
    if (action is "pre_add"):

        for msg_pk in pk_set:

            msg = Message.objects.get(pk=msg_pk)
            if msg.usuario not in instance.usuarios.all():
                print("ups , ({}) no forma parte del hilo".format(msg.usuario))
                false_pk_set.add(msg_pk)

    pk_set.difference_update(false_pk_set)


    instance.save()
m2m_changed.connect(messages_changed, sender=Hilo.mensajes.through)

