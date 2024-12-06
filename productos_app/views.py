from django.shortcuts import render,redirect
from .models import productos
# Create your views here.
def inicio_vistaProductos(request):
    losproductos=productos.objects.all()
    return render(request,"gestionarProductos.html",{"misproductos":losproductos})

def registrarProductos(request):
    id_producto=request.POST["txtid_producto"]
    nombre=request.POST["txtnombre"]
    cantidad_productos=request.POST["txtcantidad_productos"]
    precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]

    productos.objects.create(
        id_producto=id_producto,nombre=nombre,cantidad_productos=cantidad_productos,precio=precio,descripcion=descripcion
    ) #GUARDA EL REGISTRO

    return redirect("Productos")

def seleccionarProductos(request,id_producto):
    producto=productos.objects.get(id_producto=id_producto)
    return render(request, "editarProductos.html",{"misproductos":producto})

def editarProductos(request):
    id_producto=request.POST["txtid_producto"]
    nombre=request.POST["txtnombre"]
    cantidad_productos=request.POST["txtcantidad_productos"]
    precio=request.POST["txtprecio"]
    descripcion=request.POST["txtdescripcion"]
    
    producto=productos.objects.get(id_producto=id_producto)
    producto.nombre=nombre
    producto.cantidad_productos=cantidad_productos
    producto.precio=precio
    producto.descripcion=descripcion
    producto.save()  #guardar registro actualizado
    return redirect('Productos')

def borrarProductos(request,id_producto):
    producto=productos.objects.get(id_producto=id_producto)
    producto.delete() #BORRA EL REGISTRO 
    return redirect("Productos")