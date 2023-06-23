from django import forms
from django.forms import ModelForm
from .models import Computador, Cliente, Monitor, Mouse


# Crear un formulario para Computador
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('rut', 'nombre', 'direccion', 'celular', 'email')
        labels = {
            'rut': '',
            'nombre': '',
            'direccion': '',
            'celular': '',
            'email': '',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'rut'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dirección'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'celular'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        }


class MonitorForm(ModelForm):
    class Meta:
        model = Monitor
        fields = ('idProducto', 'marca', 'precioUnitario', 'resolucion', 'imagen_producto')
        labels = {
            'idProducto': '',
            'marca': '',
            'precioUnitario': '',
            'resolucion': '',
            'imagen_producto': '',

        }
        widgets = {
            'idProducto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'marca'}),
            'precioUnitario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'precio'}),
            'resolucion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'resolución'}),

        }


class ComputadorForm(ModelForm):
    class Meta:
        model = Computador
        fields = ('idProducto', 'marca', 'precioUnitario', 'cpu', 'ram', 'hdd', 'imagen_producto')
        labels = {
            'idProducto': '',
            'marca': '',
            'precioUnitario': '',
            'cpu': '',
            'ram': '',
            'hdd': '',
            'imagen_producto': '',

        }
        widgets = {
            'idProducto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'marca'}),
            'precioUnitario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'precio'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cpu'}),
            'ram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ram'}),
            'hdd': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'hdd'}),

        }


class MouseForm(ModelForm):
    class Meta:
        model = Mouse
        fields = ('idProducto', 'marca', 'precioUnitario', 'wireless', 'imagen_producto')
        labels = {
            'idProducto': '',
            'marca': '',
            'precioUnitario': '',
            'wireless': '',
            'imagen_producto': '',

        }
        widgets = {
            'idProducto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'marca'}),
            'precioUnitario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'precio'}),
            'wireless': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'wireless?'}),

        }
