from django.urls import path
from . import views
from .views import AboutPageView, ClientePageView, HomePageView, AddClientePageView, MonitorPageView, \
    AddComputadorPageView, MousePageView, ComputadorPageView, AddMonitorPageView, AddMousePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("about", AboutPageView.as_view(), name="about"),
    path("cliente", ClientePageView.as_view(), name="cliente"),
    path("monitor", MonitorPageView.as_view(), name="monitor"),
    path("mouse", MousePageView.as_view(), name="mouse"),
    path("computador", ComputadorPageView.as_view(), name="computador"),
    path("IngresarCliente", AddClientePageView.as_view(), name='ingresar-cliente'),
    path("IngresarComputador", AddComputadorPageView.as_view(), name='ingresar-computador'),
    path("IngresarMonitor", AddMonitorPageView.as_view(), name='ingresar-monitor'),
    path("IngresarMouse", AddMousePageView.as_view(), name='ingresar-mouse'),
]
