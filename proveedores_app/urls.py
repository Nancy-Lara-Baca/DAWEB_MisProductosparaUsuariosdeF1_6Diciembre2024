from django.urls import path
from proveedores_app import views


urlpatterns = [
    path('Proveedores',views.inicio_vistaProveedores, name="Proveedores"),
    path('registrarProveedores/',views.registrarProveedores,name="registrarProveedores"),
    path('seleccionarProveedores/<id_proveedor>',views.seleccionarProveedores,name="seleccionarProveedores"),
    path('editarProveedores/',views.editarProveedores,name="editarProveedores"),
    path('borrarProveedores/<id_proveedor>',views.borrarProveedores,name="borrarProveedores"),
]
