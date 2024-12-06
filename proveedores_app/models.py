from django.db import models

# Create your models here.
class proveedores(models.Model):
    id_proveedor=models.PositiveIntegerField(primary_key=True)
    id_producto=models.CharField(max_length=100)
    nombre_proveedor=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    num_telefono=models.CharField(max_length=15)

    def __str__(self):
        return self.id_proveedor