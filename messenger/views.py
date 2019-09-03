from django.shortcuts import render
from .models import Hilo
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import Http404

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
            