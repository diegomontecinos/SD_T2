
#Comando para compilar
#python -m grpc_tools.protoc -I../Protos --python_out=. --grpc_python_out=. ../Protos/Torre.proto

from concurrent import futures
import time
import random

import grpc

import Torre_pb2
import Torre_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def Revisar_pistas(pistas):

    Mejor_pista = ""
    Largo_mejor_pista = float("inf")
    #buscar pista mas corta
    for i in pistas:
        if len(pistas[i]) < Largo_mejor_pista :
            Mejor_pista = i
            Largo_mejor_pista = len(pistas[i])
    return Mejor_pista


class Aeropuerto(Torre_pb2_grpc.Serv_AeropuertoServicer):

#incializacion de los datos de la torre de control
    def __init__(self):
        print("Bienvenido a la torre de control")
        self.Nombre = input("Por favor ingrese nombre del aeropuerto: ")
        self.IP = input("Por favor ingrese la dirección IP del aeropuerto "+self.Nombre+": ")
        self.Numero_pistas = int(input("Por favor ingrese cantidad de pistas del aeropuerto "+self.Nombre+": "))
        self.Altura_de_despegue = 10000 #altura en metros
        #diccionario de pistas de Aterrizaje del aeropuerto
        self.Pistas_aterrizaje = dict()
        #self.Pistas_aterrizaje["Pista_0"] = "Pista_0"
        #diccionario de pistas de despegue
        self.Pistas_despegue = dict()
        #self.Pistas_despegue["Pista_0"] = "Pista_0"

        for i in range(self.Numero_pistas):

            self.Pistas_aterrizaje["Pista_"+str(i+1)] = list()
            self.Pistas_despegue["Pista_"+str(i+1)] = list()
        self.mas = input("¿Desea agregar destinos? [S/N] :")
        self.Destinos = dict()


        while self.mas == 'S' or self.mas == 's':
            self.nombre2 = input("ingrese el Nombre del aeropuerto de destino: ")
            self.IP2 = input("Ingrese dirección IP del aeropuerto "+self.nombre2+": ")
            self.Destinos[self.nombre2] = self.IP2
            self.mas = input("¿Desea agregar destinos? [S/N] :")

#enviar datos relacionados al despegue de un avion, previa solicitud del avion.
    def enviar_despegue(self, request, context):

        Pista = Revisar_pistas(self.Pistas_despegue)

        if len(self.Pistas_despegue[Pista]) > 0:
            Respuesta = False
            Altura = 0
            Anterior = self.Pistas_despegue[Pista][-1]
            self.Pistas_despegue[Pista].append(request.Id_avion)
            Posicion = len(self.Pistas_despegue[Pista])

        else:
            Respuesta = True
            Altura = self.Altura_de_despegue + 50
            self.Altura_de_despegue = Altura
            Anterior = "Eres el primero"
            Posicion = 0
            print("el avion "+request.Id_avion+" esta despegando por la pista "+ Pista)

        return Torre_pb2.Resp_Des(Autorizacion_despegue = Respuesta, Pista_despegue = Pista, Altura_despegue = Altura, Posicion_despegue = Posicion ,Anterior_despegue = Anterior, Ip_destino = self.Destinos[request.Name_destino], Id_avion = request.Id_avion)

    def confirmar_despegue(self, request, context):

        Pista = request.Pista_espera

        if len (self.Pistas_despegue[Pista]) > 0:

            Respuesta = False
            Altura = 0
            Posicion = self.Pistas_despegue[Pista].index(request.Id_avion) +1
            Anterior = self.Pistas_despegue[Pista][self.Pistas_despegue[Pista].index(request.Id_avion) -1]


            print ("el avion "+request.Id_avion+"Sigue esperando en la Posicion "+request.Posicion_espera)

        else:
            Respuesta = True
            Altura = self.Altura_de_despegue + 50
            self.Altura_de_despegue = Altura
            Anterior = "Eres el primero"
            Posicion = 0
            self.Pistas_despegue[request.Pista_espera].pop(0)
            print("el avion "+request.Id_avion+"Esta despegando por la pista "+request.request.Pista_espera)

        return Torre_pb2.Resp_Cons(Autorizacion_despegue = Respuesta, Pista_despegue = Pista, Altura_despegue = Altura, Posicion_despegue = Posicion, Anterior_despegue = Anterior, Ip_destino = self.Destinos[request.Name_destino], Id_avion = request.Id_avion)
    def enviar_info(self, request, context):
        return Torre_pb2.Resp_Pantalla( Salida1 = "la wea 1", A_Donde1 = "a la chucha", Pista_Salida1 = "pista 1", Hora_Salida1 = "hora del pico", Salida2 = "la wea 2", A_Donde2 = "a la chucha 2", Pista_Salida2 = "pista 2", Hora_Salida2 = "hora del pico 2", Llegda1 = "tarde 1", De_donde1 = "donde tu vieja 1", Pista_Llegada1 = "pista 3", Hora_Llegada1 = "queti 1", Llegda2 = "tarde 2", De_donde2 = "donde tu vieja 2", Pista_Llegada2 = "pista 4", Hora_Llegada2 = "queti 2")

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Torre_pb2_grpc.add_Serv_AeropuertoServicer_to_server(Aeropuerto(),server)
    server.add_insecure_port('[::]:50051')#cambiar por la ip+puerto
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
