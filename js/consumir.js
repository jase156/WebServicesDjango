var app = angular.module("app",["ngResource"]);
//Definir el controlador
app.controller("controlador",function($scope,datosAlumnos,datosMaterias){	
	$scope.listaAlumnos= datosAlumnos.get();
	$scope.listaMaterias= datosMaterias.get();


	$scope.validar = function(){
		var dato = $scope.cedula;
		var mensaje="Servicio";

		for(var i=0 ; i< $scope.listaAlumnos.length; i++){
			if ( angular.equals(dato, $scope.listaAlumnos[i].cedula)) {
				window.location.href="./materia.html";
			}
			else{
				mensaje="No se valido la cedula";
			}
		}	
		return mensaje;
	}

});
 //Definir el factori que retorne datos del webservice
 app.factory("datosAlumnos",['$resource',function($resource){
 	return $resource('http://localhost:8000/servicio/alumno',{},{get:{method:'GET', isArray:true}});
 	}
 ])
 
 app.factory("datosMaterias",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/servicio/materia/',{},{get:{method:'GET', isArray:true}});
 	}
 ])



