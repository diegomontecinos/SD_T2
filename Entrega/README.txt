para ejecutar el programa:

*Compilacion en c# (Aviones):

#Instalar VisualStudio
#Instalar Microsoft.NetCore

Directorio = ./SD_T2/Entrega/Avion

Utilizando VisualStudio 2017:
	-Abrir el proyecto Avion.sln
	-Compilar la solucion
	-Ejecutar la solucion
___________________________________________
*Compilacion Python(Torres de control):

#Instalar python 3.6

Directorio = ./SD_T2/Entrega/Torre

Desde el directorio abrir una terminal y ejecutar python .\Torre_server.py
____________________________________________
*Ejecucion Node.js(Pantallas)

Directorio = ./SD_T2/Entrega/Node

Desde el directorio abrir una terminal y ejecutar node .\Pantalla.js 
____________________________________________

Compilacion Protos

#Instalar archivos necesarios desde los siguientes links:
https://github.com/protocolbuffers/protobuf
https://github.com/grpc/grpc



c#
generate_protos.bat

Python
python -m grpc_tools.protoc -I../Protos --python_out=. --grpc_python_out=. ../Protos/Torre.proto

Node
No lo necesita.

PD: ya est� todo compilado


Las Instrucciones antes mencionadas fueron porbadas en Windows 10 64b, en otros S.O se debe utilizar comandos equivalentes.


Una vez que el programa se encuentre en ejecuci�n:
	la torre de control le pedir� que ingrese los siguientes datos: 
		el nombre del aeropuerto, la ip del aeropuerto, la cantidad de pistas del aeropuero, 
		para esta implementaci�n se considera que la cantidad de pistas de aterrizaje es igual a las pistas de despegue.
		Luego, se pedir� el ingreso de m�s destinos.
	
	los aviones le pedir� que ingrese los siguientes datos:
		la IP de la torre de control inicial, la ID del avi�n, el cual correspode al n�mero de avi�n,
		Luego le indicara el estado del despegue.
	
	