from django.db import models

# Create your models here.
class envio(models.Model):
    id_envio=models.AutoField(primary_key=True)
    id_cliente=models.IntegerField()
    id_empleado=models.IntegerField()
    id_producto=models.IntegerField()
    fecha_pedido = models.DateField()
    cantidad_productos=models.IntegerField()
    total=models.IntegerField()

    def __str__(self): 
        return self.id_envio