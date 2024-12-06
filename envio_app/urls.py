from django.urls import path
from envio_app import views


urlpatterns = [
    path('Envios',views.inicio_vistaEnvios, name="Envios"),
    path('registrarEnvios/',views.registrarEnvios,name="registrarEnvios"),
    path('seleccionarEnvios/<id_envio>',views.seleccionarEnvios,name="seleccionarEnvios"),
    path('editarEnvios/',views.editarEnvios,name="editarEnvios"),
    path('borrarEnvios/<id_envio>',views.borrarEnvios,name="borrarEnvios"),
]
