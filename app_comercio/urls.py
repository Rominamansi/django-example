from django.urls import path
from . import views
from .views import AboutPageView, ClientePageView, HomePageView, AddClientePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("about", AboutPageView.as_view(), name="about"),
    path("cliente", ClientePageView.as_view(), name="cliente"),
    path("IngresarCliente", AddClientePageView.as_view(), name='ingresar-cliente'),
]
