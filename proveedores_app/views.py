from django.shortcuts import render,redirect
from .models import proveedores
# Create your views here.
def inicio_vistaProveedores(request):
    losproveedores=proveedores.objects.all()
    return render(request,"gestionarProveedores.html",{"misproveedores":losproveedores})

def registrarProveedores(request):
    id_proveedor=request.POST["txtid_proveedor"]
    id_producto=request.POST["txtid_producto"]
    nombre_proveedor=request.POST["txtnombre_proveedor"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]

    proveedores.objects.create(
        id_proveedor=id_proveedor,id_producto=id_producto,nombre_proveedor=nombre_proveedor,direccion=direccion,num_telefono=num_telefono
    ) #GUARDA EL REGISTRO

    return redirect("Proveedores")

def seleccionarProveedores(request,id_proveedor):
    proveedor=proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedores.html",{"misproveedores":proveedor})

def editarProveedores(request):
    id_proveedor=request.POST["txtid_proveedor"]    
    id_producto=request.POST["txtid_producto"]
    nombre_proveedor=request.POST["txtnombre_proveedor"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["txtnum_telefono"]
    
    proveedor=proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.id_producto=id_producto
    proveedor.nombre_proveedor=nombre_proveedor
    proveedor.direccion=direccion
    proveedor.num_telefono=num_telefono
    proveedor.save()  #guardar registro actualizado
    return redirect('Proveedores')

def borrarProveedores(request,id_proveedor):
    proveedor=proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.delete() #BORRA EL REGISTRO 
    return redirect("Proveedores")