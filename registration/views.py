from .forms import UserCreationEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.


class Register_view(CreateView):

    form_class = UserCreationEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):

        return reverse_lazy('login') + '?1'

    def get_form(self):

        form = super(Register_view,self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control nb-2','placeholder':'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control nb-2','placeholder':'email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control nb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control nb-2','placeholder':'Repita su Contraseña'})
        
        return form




    



