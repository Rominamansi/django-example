from django.db import models


class Producto(models.Model):
    idProducto = models.BigIntegerField(primary_key=True)
    marca = models.CharField(max_length=120)
    precioUnitario = models.IntegerField()

    class Meta:
        abstract = True


class Mouse(Producto):
    wireless = models.BooleanField()

    def __str__(self):
        return self.idProducto + " - Mouse"


class Monitor(Producto):
    resolucion = models.CharField(max_length=10)

    def __str__(self):
        return self.idProducto + "  - Monitor"


class Computador(Producto):
    cpu = models.CharField(max_length=5)
    ram = models.IntegerField()
    hdd = models.IntegerField()

    def __str__(self):
        return self.idProducto + "  - Computador"


class Cliente(models.Model):
    rut = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=120)
    direccion = models.TextField()
    celular = models.IntegerField()
    email = models.EmailField()
    compraMouse = models.ManyToManyField(Mouse, blank=True)
    compraComputador = models.ManyToManyField(Computador, blank=True)
    compraMonitor = models.ManyToManyField(Monitor, blank=True)

    def __str__(self):
        return str(self.rut) + " - " + self.nombre
