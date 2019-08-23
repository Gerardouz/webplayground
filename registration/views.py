from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class SignUpView(CreateView):

    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):

        return reverse_lazy('login') + '?1'

    def get_form(self, form_class = None ):

        form = super(SignUpView,self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control nb-2','placeholder':'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control nb-2','placeholder':'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control nb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control nb-2','placeholder':'Repita su Contraseña'})
        
        return form

@method_decorator(login_required, name = 'dispatch')
class ProfileUpdate(TemplateView):

    template_name = "registration/profile_form.html"




