from django.contrib.messages.views import SuccessMessageMixin
from django.core.checks import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ClienteForm, MonitorForm, ComputadorForm, MouseForm
from .models import Cliente, Monitor, Mouse, Computador


class HomePageView(TemplateView):
    # def homePageView(request):
    template_name = "home.html"
    # return HttpResponse("Hola, Mundo!")


class AboutPageView(TemplateView):
    # def homePageView(request):
    template_name = "about.html"


class ClientePageView(ListView):
    model = Cliente
    template_name = "cliente.html"
    context_object_name = 'data'


class MonitorPageView(ListView):
    model = Monitor
    template_name = "monitor.html"
    context_object_name = 'data'


class MousePageView(ListView):
    model = Mouse
    template_name = "mouse.html"
    context_object_name = 'data'


class ComputadorPageView(ListView):
    model = Computador
    template_name = "computador.html"
    context_object_name = 'data'


class AddClientePageView(SuccessMessageMixin, CreateView):
    form_class = ClienteForm
    template_name = 'IngresarCliente.html'
    success_message = 'Cliente Ingresado'
    error_message = "Error en ingresar a un cliente"
    success_url = reverse_lazy("ingresar-cliente")

    def get_success_url(self):
        return reverse('ingresar-cliente')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AddMonitorPageView(SuccessMessageMixin, CreateView):
    form_class = MonitorForm
    template_name = 'IngresarMonitor.html'
    success_message = 'Monitor Ingresado'
    error_message = "Error en ingresar a un monitor"
    success_url = reverse_lazy("ingresar-monitor")

    def get_success_url(self):
        return reverse('ingresar-monitor')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AddComputadorPageView(SuccessMessageMixin, CreateView):
    form_class = ComputadorForm
    template_name = 'IngresarComputador.html'
    success_message = 'Computador Ingresado'
    error_message = "Error en ingresar a un computador"
    success_url = reverse_lazy("ingresar-computador")

    def get_success_url(self):
        return reverse('ingresar-computador')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AddMousePageView(SuccessMessageMixin, CreateView):
    form_class = MouseForm
    template_name = 'IngresarMouse.html'
    success_message = 'Mouse Ingresado'
    error_message = "Error en ingresar a un mouse"
    success_url = reverse_lazy("ingresar-mouse")

    def get_success_url(self):
        return reverse('ingresar-mouse')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
