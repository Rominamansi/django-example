from django.contrib import admin

from .models import Cliente, Mouse, Monitor, Computador
admin.site.register(Cliente)
admin.site.register(Mouse)
admin.site.register(Monitor)
admin.site.register(Computador)
