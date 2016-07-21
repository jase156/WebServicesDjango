from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import FormularioMaterias,FormularioAlumnos
from .models import Materia,Alumnos,Registros
# Create your views here.
def listar(request):
	alumno=Alumnos.objects.all()
	materia=Materia.objects.all()
	context={
 	'alumno':alumno,
 	'materia':materia,
 	}
	return render(request,'listar.html',context)	

def crearAlum(request):
	f = FormularioAlumnos(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			n = datos.get("nombre")
			a = datos.get("apellido")
			c = datos.get("cedula")
			co = datos.get("email")
			di = datos.get("direccion")
			obj = Alumnos.objects.create(cedula=c,nombre=n,apellido=a,email=co,direccion=di)
			if obj:
				return redirect(listar)
	context ={
		'f':f,
	}
	return render(request,"crearAlumno.html",context)

def crearMateria(request):
	f = FormularioMaterias(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			n = datos.get("nombre")
			c = datos.get("codigo")
			cup= datos.get("cupos")
			obj = Materia.objects.create(nombre=n,codigo=c,cupos=cup)
			if obj:
				return redirect(listar)
	context ={
		'f':f,
	}
	return render(request,"crearMateria.html",context)




def modificarMateria(request):
	#f = FormularioModificarCliente(request.POST or None)	
	f = FormularioMaterias(request.POST or None)
	materia = Materia.objects.get(codigo=request.GET['codigo'])
	context={
		'materia':materia,
		'f':f,
	}
	f.fields['nombre'].initial = materia.nombre
	f.fields['codigo'].initial=materia.codigo
	f.fields['matriculados'].initial=materia.matriculados
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			materia.codigo = datos.get("codigo")
			materia.nombres = datos.get("nombre")
			materia.matriculados = datos.get("matriculados")

			if (materia.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado La materia", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el materia", fail_silently=True)
			return redirect(listar)
	
	return render(request,"modificarMateria.html",context)


def modificarAlumno(request):
	#f = FormularioModificarCliente(request.POST or None)	
	f = FormularioAlumnos(request.POST or None)
	alumno = Alumnos.objects.get(cedula=request.GET['cedula'])
	context={
		'alumno':alumno,
		'f':f,
	}
	f.fields['cedula'].initial = "Ignore"
	f.fields['nombre'].initial = alumno.nombre
	f.fields['apellido'].initial = alumno.apellido
	f.fields["email"].initial = alumno.email
	f.fields["direccion"].initial = alumno.direccion
	
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			alumno.nombres = datos.get("nombre")
			alumno.apellidos = datos.get("apellido")
			alumno.direccion = datos.get("direccion")
			alumno.email= datos.get("email")
			if (alumno.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el Alumno", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el Alumno", fail_silently=True)
			return redirect(listar)
	return render(request,"modificarAlumno.html",context)



def eliminarMateria(request):
	materia = Materia.objects.get(codigo=request.GET['codigo'])
	context = {
		'materia':materia,
	}

	return render(request,"eliminarMateria.html",context)

def eliminarAlumno(request):
	alumno = Alumnos.objects.get(cedula=request.GET['cedula'])
	context = {
		'alumno':alumno,
	}

	return render(request,"eliminarAlumno.html",context)

def eliminarAlum(request):
	alumno = Alumnos.objects.get(cedula=request.GET['cedula'])
	if alumno.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el alumno", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el alumno", fail_silently=True)
	return redirect(listar)

def eliminarMat(request):
	codigo = Materia.objects.get(codigo=request.GET['codigo'])
	if codigo.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el Materia", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el Materia", fail_silently=True)
	return redirect(listar)


def matricular(request):
	alumno=Alumnos.objects.get(cedula=request.GET['cedula'])
	materia=Materia.objects.all()
	context={
		'alumno':alumno,
		'materia':materia
	}
	return render(request,"matricular.html",context)

