from django.shortcuts import render,redirect
from .models import envio
# Create your views here.
def inicio_vistaEnvios(request):
    losenvios=envio.objects.all()
    return render(request,"gestionarEnvio.html",{"misenvios":losenvios})

def registrarEnvios(request):
    id_envio=request.POST["numid_envio"]
    id_cliente=request.POST["numid_cliente"]
    id_empleado=request.POST["numid_empleado"]
    id_producto=request.POST["numid_producto"]
    fecha_pedido=request.POST["txtfecha_pedido"]
    cantidad_productos=request.POST["numcantidad_productos"]
    total=request.POST["numtotal"]

    envio.objects.create(
        id_envio=id_envio,id_cliente=id_cliente,id_empleado=id_empleado,id_producto=id_producto,fecha_pedido=fecha_pedido,cantidad_productos=cantidad_productos,total=total,
    ) #GUARDA EL REGISTRO

    return redirect("Envios")

def seleccionarEnvios(request,id_envio):
    envios=envio.objects.get(id_envio=id_envio)
    return render(request, "editarEnvio.html",{"misenvios":envios})

def editarEnvios(request):
    id_envio=request.POST["numid_envio"]
    id_cliente=request.POST["numid_cliente"]
    id_empleado=request.POST["numid_empleado"]
    id_producto=request.POST["numid_producto"]
    fecha_pedido=request.POST["txtfecha_pedido"]
    cantidad_productos=request.POST["numcantidad_productos"]
    total=request.POST["numtotal"]
    
    envios=envio.objects.get(id_envio=id_envio)
    envios.id_cliente=id_cliente
    envios.id_empleado=id_empleado
    envios.id_producto=id_producto
    envios.fecha_pedido=fecha_pedido
    envios.cantidad_productos=cantidad_productos
    envios.total=total
    envios.save()  #guardar registro actualizado
    return redirect('Envios')

def borrarEnvios(request,id_envio):
    envios=envio.objects.get(id_envio=id_envio)
    envios.delete() #BORRA EL REGISTRO 
    return redirect("Envios")