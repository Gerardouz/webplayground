from django.shortcuts import render
from .models import Hilo, Message
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.
@method_decorator(login_required, name= 'dispatch')
class HiloView(TemplateView):

    template_name = "messenger/hilo_list.html"

    def get_queryset(self):

        queryset = super(HiloView, self).get_queryset()
        return queryset.filter(usuarios=self.request.user)
@method_decorator(login_required, name= 'dispatch')
class HiloDetailView(DetailView):

    model = Hilo

    def get_object(self):

        obj = super(HiloDetailView, self).get_object()  

        if (self.request.user not in obj.usuarios.all()):
            raise Http404
        return obj

def add_mensaje(request,pk):

    json_responsive = {'creado':False}

    if (request.user.is_authenticated):
        content = request.GET.get('content',None)
        if (content):

            hilo = get_object_or_404(Hilo,pk=pk)
            mensaje = Message.objects.create(usuario=request.user,contenido=content)
            hilo.mensajes.add(mensaje)
            json_responsive['creado'] = True
            if(len(hilo.mensajes.all()) is 1):
                json_responsive['first'] = True
    else:
        raise Http404("Usuario no Identificado")

    return JsonResponse(json_responsive)

@login_required
def start_message(request,username):

    user = get_object_or_404(User, username=username)
    thread = Hilo.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('thread_detail',args=[thread.pk]))




