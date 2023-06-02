from django.urls import path
from . import views
from .views import AboutPageView, ClientePageView, HomePageView, AddClientePageView, MonitorPageView, \
    ComputadorPageView, MousePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("about", AboutPageView.as_view(), name="about"),
    path("cliente", ClientePageView.as_view(), name="cliente"),
    path("monitor", MonitorPageView.as_view(), name="monitor"),
    path("mouse", MousePageView.as_view(), name="mouse"),
    path("computador", ComputadorPageView.as_view(), name="computador"),
    path("IngresarCliente", AddClientePageView.as_view(), name='ingresar-cliente'),
]
