from django import forms
from django.forms import ModelForm
from .models import Computador, Cliente


# Crear un formulario para Computador
class ComputadorForm(ModelForm):
    class Meta:
        model = Computador
        fields = "__all__"


# Crear un formulario para Computador
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('rut', 'nombre', 'direccion', 'celular', 'email')
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
