from django.db import models

# Create your models here.
class empleados(models.Model):
    id_empleado=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    num_telefono=models.IntegerField()
    fecha_nacimiento=models.DateField()
    fecha_ingreso=models.DateField()
    puesto=models.CharField(max_length=50)
    salario=models.PositiveBigIntegerField()

    def __str__(self):
        return self.nombre