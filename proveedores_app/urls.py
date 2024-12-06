from django.urls import path
from proveedores_app import views


urlpatterns = [
    path('Proveedores',views.inicio_vistaProveedores, name="Proveedores"),
    path('registrarProveedores/',views.registrarProveedores,name="Registrar Proveedores"),
    path('seleccionarProveedores/<id_proveedor>',views.seleccionarProveedores,name="Seleccionar Proveedores"),
    path('editarProveedores/',views.editarProveedores,name="Editar Proveedores"),
    path('borrarProveedores/<id_proveedor>',views.borrarProveedores,name="Borrar Proveedores"),
]
