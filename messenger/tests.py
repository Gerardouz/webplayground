from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Hilo

# Create your tests here.

class HiloTestCase(TestCase):

    def setUp(self):

        self.user1 = User.objects.create_user('user1',None,'test1234')
        self.user2 = User.objects.create_user('user2',None,'test1234')


        self.hilo = Hilo.objects.create()

    def test_add_users(self):

        self.hilo.usuarios.add(self.user1,self.user2)
        self.assertEqual(len(self.hilo.usuarios.all()),2)

    def test_filter_thread(self):
        self.hilo.usuarios.add(self.user1,self.user2)
        threads = Hilo.objects.filter(usuarios=self.user1).filter(usuarios=self.user2)
        self.assertEqual(self.hilo, threads[0])

    def test_filter_non_exists(self):
        threads = Hilo.objects.filter(usuarios=self.user1).filter(usuarios=self.user2)
        self.assertEqual(len(threads),0)



    def test_add_message(self):
        self.hilo.usuarios.add(self.user1,self.user2)
        message1 = Message.objects.create(usuario=self.user1, contenido='muy buenas')
        message2 = Message.objects.create(usuario=self.user2, contenido='hola')
        self.hilo.mensajes.add(message1,message2)
        self.assertEqual(len(self.hilo.mensajes.all()), 2)

        for message in self.hilo.mensajes.all():
            print ("({}) : ({})".format(message.usuario,message.contenido))