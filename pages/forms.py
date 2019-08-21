from django import forms
from .models import Page

class PageForm(forms.ModelForm):


    class Meta():

        model = Page
        fields = ['titulo','contenido','orden']

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un Titulo'}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
            'orden': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'', 'order':'', 'content': ''
        }