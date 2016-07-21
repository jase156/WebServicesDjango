from django import forms
from .models import Materia,Alumnos

class FormularioMaterias(forms.ModelForm):
	class Meta:
		model=Materia
		fields=['nombre','codigo','cupos']

class FormularioAlumnos(forms.ModelForm):
	class Meta:
		model=Alumnos
		fields=['cedula','nombre','apellido','email','direccion']