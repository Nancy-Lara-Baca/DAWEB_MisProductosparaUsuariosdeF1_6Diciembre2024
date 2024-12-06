from django.urls import path
from empleados_app import views


urlpatterns = [
    path('Empleados',views.inicio_vistaEmpleados, name="Empleados"),
    path('registrarEmpleados/',views.registrarEmpleados,name="registrarEmpleados"),
    path('seleccionarEmpleados/<int:id_empleado>',views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path('editarEmpleados/',views.editarEmpleados,name="editarEmpleados"),
    path('borrarEmpleados/<int:id_empleado>',views.borrarEmpleados,name="borrarEmpleados"),
]
