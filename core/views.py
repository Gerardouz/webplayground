from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage_View(TemplateView):

    template_name = "core/home.html" 

    def get(self, request, *args, **kwargs):
        return render (request, self.template_name , {'titulo':'mi super web playground'})
    
class SamplePage_view(TemplateView):
     template_name = "core/sample.html" 
 