from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ClienteForm, MonitorForm, ComputadorForm, MouseForm
from .models import Cliente, Monitor, Mouse, Computador


class HomePageView(TemplateView):

    template_name = "home.html"


class AboutPageView(TemplateView):

    template_name = "about.html"


class ClientePageView(ListView):

    model = Cliente
    template_name = "cliente.html"
    context_object_name = 'data'
    http_method_names = ['get', 'post']


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


class DeleteClientView(View):

    template_name = 'cliente.html'
    success_url = 'cliente'

    def post(self, request):
        selected_items = request.POST.getlist('selected_items')

        # Validate and sanitize the selected_items
        try:
            selected_items = list(map(int, selected_items))  # Convert to a list of integers
        except ValueError:
            raise Http404("Invalid input for selected_items")

        # Perform the deletion
        if selected_items:
            Cliente.objects.filter(rut__in=selected_items).delete()

        return redirect(self.success_url)  # Redirect to a success page or another view

    def get(self, request):
        clientes = Cliente.objects.all()
        return  render(request, self.template_name,{'clientes':clientes})
class DeleteMonitorView(View):

    template_name = 'monitor.html'
    success_url = 'monitor'

    def post(self, request):
        selected_items = request.POST.getlist('selected_items')

        # Validate and sanitize the selected_items
        try:
            selected_items = list(map(int, selected_items))  # Convert to a list of integers
        except ValueError:
            raise Http404("Invalid input for selected_items")

        # Perform the deletion
        if selected_items:
            Monitor.objects.filter(idProducto__in=selected_items).delete()

        return redirect(self.success_url)  # Redirect to a success page or another view

    def get(self, request):
         monitores = Monitor.objects.all()
        return  render(request, self.template_name,{'monitores':monitores})
class DeleteMouseView(View):

    template_name = 'mouse.html'
    success_url = 'mouse'

    def post(self, request):
        selected_items = request.POST.getlist('selected_items')

        # Validate and sanitize the selected_items
        try:
            selected_items = list(map(int, selected_items))  # Convert to a list of integers
        except ValueError:
            raise Http404("Invalid input for selected_items")

        # Perform the deletion
        if selected_items:
            Mouse.objects.filter(idProducto__in=selected_items).delete()

        return redirect(self.success_url)  # Redirect to a success page or another view

    def get(self, request):
        mouse = Mouse.objects.all()
        return  render(request, self.template_name,{'mouse':mouse})
        

class DeleteComputadorView(View):

    template_name = 'computador.html'
    success_url = 'computador'

    def post(self, request):
        selected_items = request.POST.getlist('selected_items')

        # Validate and sanitize the selected_items
        try:
            selected_items = list(map(int, selected_items))  # Convert to a list of integers
        except ValueError:
            raise Http404("Invalid input for selected_items")

        # Perform the deletion
        if selected_items:
            Computador.objects.filter(idProducto__in=selected_items).delete()

        return redirect(self.success_url)  # Redirect to a success page or another view

    def get(self, request):
        computadores = Computador.objects.all()
        return  render(request, self.template_name,{'computadores':computadores})

