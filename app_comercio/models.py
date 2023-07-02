from django.db import models


class Producto(models.Model):
    idProducto = models.BigIntegerField(primary_key=True)
    marca = models.CharField(max_length=120)
    precioUnitario = models.IntegerField()
    imagen_producto = models.ImageField(null=True, blank=True, upload_to="images/")

    def image_url(self):
        if self.imagen_producto and self.imagen_producto.name:
            return '/media/' + self.imagen_producto.name
        else:
            return None

    class Meta:
        abstract = True


class Mouse(Producto):
    wireless = models.BooleanField()

    def __str__(self):
        return str(self.idProducto) + " - Mouse"


class Monitor(Producto):
    resolucion = models.CharField(max_length=10)

    def __str__(self):
        return str(self.idProducto) + "  - Monitor"


class Computador(Producto):
    cpu = models.CharField(max_length=5)
    ram = models.IntegerField()
    hdd = models.IntegerField()

    def __str__(self):
        return str(self.idProducto) + "  - Computador"


class Cliente(models.Model):
    rut = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=120)
    direccion = models.TextField()
    celular = models.IntegerField()
    email = models.EmailField()
    imagen_cliente = models.ImageField(null=True, blank=True, upload_to="images/")
    compraMouse = models.ManyToManyField(Mouse, blank=True)
    compraComputador = models.ManyToManyField(Computador, blank=True)
    compraMonitor = models.ManyToManyField(Monitor, blank=True)
    selected = models.BooleanField(default=False)
    
    def image_url(self):
        if self.imagen_cliente and self.imagen_cliente.name:
            return '/media/' + self.imagen_cliente.name
        else:
            return None

    objects = models.Manager()

    def __str__(self):
        return str(self.rut) + " - " + self.nombre
