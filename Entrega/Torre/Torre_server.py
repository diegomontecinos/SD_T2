
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

        if len(self.Pistas[Pista]) > 0:
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

        return Torre_pb2.Resp_Des(Autorizacion_despegue = Respuesta, Pista_despegue = Pista, Altura_despegue = Altura, Posicion_despegue = Posicion ,Anterior_despegue = Anterior, Ip_destino= request.Name_destino, Id_avion = request.Id_avion)

    def confirmar_despegue(self, request, context):
        print("la wea")

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
