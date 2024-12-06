from django.shortcuts import render,redirect
from .models import empleados
# Create your views here.
def inicio_vistaEmpleados(request):
    losempleados=empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleados(request):
    id_empleado=request.POST["numid_empleado"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["numnum_telefono"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]
    puesto=request.POST["txtpuesto"]
    salario=request.POST["numsalario"]

    empleados.objects.create(
        id_empleado=id_empleado,nombre=nombre,direccion=direccion,num_telefono=num_telefono,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,puesto=puesto,salario=salario
    ) #GUARDA EL REGISTRO

    return redirect("Empleados")

def seleccionarEmpleados(request,id_empleado):
    empleado=empleados.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleados.html",{"misempleados":empleado})

def editarEmpleados(request):
    id_empleado=request.POST["numid_empleado"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    num_telefono=request.POST["numnum_telefono"]
    fecha_nacimiento=request.POST["txtfecha_nacimiento"]
    fecha_ingreso=request.POST["txtfecha_ingreso"]
    puesto=request.POST["txtpuesto"]
    salario=request.POST["numsalario"]
    
    empleado=empleados.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.direccion=direccion
    empleado.num_telefono=num_telefono
    empleado.fecha_nacimiento=fecha_nacimiento
    empleado.fecha_ingreso=fecha_ingreso
    empleado.puesto=puesto
    empleado.salario=salario
    empleado.save()  #guardar registro actualizado
    return redirect('Empleados')

def borrarEmpleados(request,id_empleado):
    empleado=empleados.objects.get(id_empleado=id_empleado)
    empleado.delete() #BORRA EL REGISTRO 
    return redirect("Empleados")