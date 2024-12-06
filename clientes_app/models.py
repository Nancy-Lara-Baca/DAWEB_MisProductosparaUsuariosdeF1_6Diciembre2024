from django.db import models

# Create your models here.
class clientes(models.Model):
    id_cliente=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    num_telefono=models.IntegerField()
    correo=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return self.id_cliente