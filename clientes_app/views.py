from django.shortcuts import render,redirect
from .models import clientes
# Create your views here.
def inicio_vistaClientes(request):
    losclientes=clientes.objects.all()
    return render(request,"gestionarClientes.html",{"misclientes":losclientes})

def registrarClientes(request):
    id_cliente=request.POST["numid_cliente"]
    nombre=request.POST["txtnombre"]
    num_telefono=request.POST["numnum_telefono"]
    correo=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]

    clientes.objects.create(
        id_cliente=id_cliente,nombre=nombre,num_telefono=num_telefono,correo=correo,direccion=direccion,fecha_nacimiento=fecha_nacimiento,
    ) #GUARDA EL REGISTRO

    return redirect("Clientes")

def seleccionarClientes(request,id_cliente):
    cliente=clientes.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html",{"misclientes":cliente})

def editarClientes(request):
    id_cliente=request.POST["numid_cliente"]
    nombre=request.POST["txtnombre"]
    num_telefono=request.POST["numnum_telefono"]
    correo=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]

    cliente=clientes.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.num_telefono=num_telefono
    cliente.correo=correo
    cliente.direccion=direccion
    cliente.fecha_nacimiento=fecha_nacimiento
    cliente.save()  #guardar registro actualizado
    return redirect('Clientes')

def borrarClientes(request,id_cliente):
    cliente=clientes.objects.get(id_cliente=id_cliente)
    cliente.delete() #BORRA EL REGISTRO 
    return redirect("Clientes")