#transformar los obejetos y dar priopedades para que se pueda representar en otros formatos
from registro.models import  Alumnos, Materia
from rest_framework import serializers

class AlumnosSerializable(serializers.ModelSerializer):
	class Meta:
		model=Alumnos
		fields=['cedula','nombre','apellido','email','direccion']
class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model=Materia
		fields=['nombre','codigo','cupos']