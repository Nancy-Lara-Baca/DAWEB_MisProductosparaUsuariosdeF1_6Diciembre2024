from django.urls import path
from local_app import views


urlpatterns = [
    path('Local',views.inicio_vistaLocal, name="Local"),
    path('registrarLocal/',views.registrarLocal,name="registrarLocal"),
    path('seleccionarLocal/<id_local>',views.seleccionarLocal,name="seleccionarLocal"),
    path('editarLocal/',views.editarLocal,name="editarLocal"),
    path('borrarLocal/<id_local>',views.borrarLocal,name="borrarLocal"),
]
