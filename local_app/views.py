from django.shortcuts import render,redirect
from .models import local
# Create your views here.
def inicio_vistaLocal(request):
    loslocales=local.objects.all()
    return render(request,"gestionarLocal.html",{"mislocales":loslocales})

def registrarLocal(request):
    id_local=request.POST["numid_local"]
    direccion=request.POST["txtdireccion"]
    gerente=request.POST["txtgerente"]
    empleados=request.POST["numempleados"]
    cantidad_productos=request.POST["numcantidad_productos"]
    num_telefono=request.POST["numnum_telefono"]

    local.objects.create(
        id_local=id_local,direccion=direccion,gerente=gerente,empleados=empleados,cantidad_productos=cantidad_productos,num_telefono=num_telefono
    ) #GUARDA EL REGISTRO

    return redirect("Local")

def seleccionarLocal(request,id_local):
    Local=local.objects.get(id_local=id_local)
    return render(request, "editarLocal.html",{"mislocales":Local})

def editarLocal(request):
    id_local=request.POST["numid_local"]
    direccion=request.POST["txtdireccion"]
    gerente=request.POST["txtgerente"]
    empleados=request.POST["numempleados"]
    cantidad_productos=request.POST["numcantidad_productos"]
    num_telefono=request.POST["numnum_telefono"]
    
    Local=local.objects.get(id_local=id_local)
    Local.direccion=direccion
    Local.gerente=gerente
    Local.empleados=empleados
    Local.cantidad_productos=cantidad_productos
    Local.num_telefono=num_telefono
    Local.save()  #guardar registro actualizado
    return redirect('Local')

def borrarLocal(request,id_local):
    Local=local.objects.get(id_local=id_local)
    Local.delete() #BORRA EL REGISTRO 
    return redirect("Local")