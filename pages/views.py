from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
"""
class StaffMixin(object):

    
    def dispatch(self,request,*args,**kwargs):

        return super(StaffMixin, self).dispatch(request, *args, **kwargs)
"""

# Create your views here.
class PagesList_view(ListView):
    model = Page

class PageDetail_view(DetailView):
    model = Page


@method_decorator(staff_member_required,name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages')


@method_decorator(staff_member_required,name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages')


    def get_success_url(self):

        return reverse_lazy('page_update', args = [self.object.id]) + '?1'
@method_decorator(staff_member_required,name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')





    