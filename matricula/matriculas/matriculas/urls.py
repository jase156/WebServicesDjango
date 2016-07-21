"""matriculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from webServices.views import AlumnosViewSet, MateriaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'alumno',AlumnosViewSet)
router.register(r'materia',MateriaViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'registro.views.listar'),
    url(r'^crearAlumno/$', 'registro.views.crearAlum'),
    url(r'^crearMateria/$', 'registro.views.crearMateria'),
    url(r'^modificarAlumno/$', 'registro.views.modificarAlumno'),
    url(r'^modificarMateria/$', 'registro.views.modificarMateria'),
    url(r'^eliminarAlumno/$', 'registro.views.eliminarAlumno'),
    url(r'^eliminarMateria/$', 'registro.views.eliminarMateria'),
	url(r'^eliminarAlum/$', 'registro.views.eliminarAlum'),
	url(r'^eliminarMat/$', 'registro.views.eliminarMat'),
    url(r'^matricular/$', 'registro.views.matricular'),
    url(r'^servicio/', include(router.urls)), 
]

