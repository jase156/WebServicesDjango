from django.shortcuts import render
from registro.models import Alumnos, Materia
from .serializable import AlumnosSerializable, MateriaSerializable
from rest_framework import viewsets

class AlumnosViewSet(viewsets.ModelViewSet):
	# llamo objeto serializable
	serializer_class = AlumnosSerializable
	#defino la consulta de datos que se enviaran en el webservices
	queryset = Alumnos.objects.all()

class MateriaViewSet(viewsets.ModelViewSet):
	# llamo objeto serializable
	serializer_class = MateriaSerializable
	#defino la consulta de datos que se enviaran en el webservices
	queryset = Materia.objects.filter(matriculados__lte=29)