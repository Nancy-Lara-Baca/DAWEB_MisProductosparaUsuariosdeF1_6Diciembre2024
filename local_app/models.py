from django.db import models

# Create your models here.
class local(models.Model):
    id_local=models.PositiveIntegerField(primary_key=True)
    direccion=models.CharField(max_length=50)
    gerente=models.CharField(max_length=100)
    empleados=models.CharField(max_length=15)
    cantidad_productos=models.CharField(max_length=50)
    num_telefono=models.CharField(max_length=15)

    def __str__(self):
        return self.id_local