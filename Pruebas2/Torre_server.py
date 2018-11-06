from concurrent import futures
import time
import random

import grpc

import Torre_pb2
import Torre_pb2_grpc

#def asignar_pista():

#def asignar_altura():



def despegar(flag,pos,anterior):
    with grpc.insecure_channel('localhost:50051') as channel: #cambiar por ip+puerto
        stub = Aeropuerto_pb2_grpc.PDespegueStub(channel)
        if flag == 0:
            response = stub.enviar_despegue(Aeropuerto_pb2.Pista_Des(autorizacion_despegue = False, Pista_despegue = asignar_pista(), altura_despegue = asignar_altura(),posicion_despegue = pos,anterior_despegue = anterior))
        else:
            response = stub.enviar_despegue(Aeropuerto_pb2.Pista_Des(autorizacion_despegue = True, Pista_despegue = asignar_pista(), altura_despegue = asignar_altura(),posicion_despegue = pos,anterior_despegue = anterior))


class PDespegue(Torre_pb2_grpc.PDespegueServicer):
    def __init__(self):
        print("Bienvenido a la torre de control")
        self.nombre = input("Por favor ingrese nombre del aeropuerto: ")
        self.IP = input("Por favor ingrese la dirección IP del aeropuerto "+nombre+": ")
        self.pistas = input("Por favor ingrese cantidad de pistas del aeropuerto "+nombre+": ")
        self.Pentrada = dict()
        self.Pentrada["Pista 0"] = "Pista 0"
        self.Psalidas = dict()
        self.Psalidas["Pista 0"] = "Pista 0"
        for i in range(pistas):
            self.Pentrada["Pista "+str(i+1)] = list()
            self.Psalidas["Pista "+str(i+1)] = list()
        self.mas = input("¿Desea agregar destinos? [S/N] :")
        self.destinos = dict()
        #flag para pistas de Aterrizaje
        #flag para pistas de Despegue
        #cola de Despegue
        #self.colaDesp = list()
        #self.colaAt = list()
        #cola de Aterrizaje
        while mas == 'S' or mas == 's':
            self.nombre2 = input("ingrese sonmbre de nuevo destino: ")
            self.IP2 = input("Ingrese dirección IP del aeropuerto "+nombre2+": ")
            self.destinos[nombre2] = IP2
            self.mas = input("¿Desea agregar destinos? [S/N] :")

    def enviar_despegue (self, request, context):
        for i in range(self.pistas):
            if len(self.Pentrada["Pista "+str(i+1)])<self.pistas:
                #if() revisar si está en esa lista y sacarlo de ahúí
                #sacarlo de la cola
                return despegar(1,-1,"nadie")
                #break
        #anterior = colaDesp[-1] ver bien como ver el anterior
        aux = self.Pentrada["Pista 0"]

        self.Pentrada[aux].append(self.nombre)#es el nombre del avion
        pos = len(self.Pentrada[aux])-1
        return despegar(0,pos,anterior)

    def enviar_aterrizaje (self, request, context):
        for i in range(self.pistas):
            if len(self.Psalidas["Pista "+str(i+1)])<self.pistas:
                #ver si está en esa cola y sacarlo
                return aterrizar(1,(i+1),"nadie")

        aux = self.Psalidas["Pista 0"]
        self.Psalidas[aux].append() #nombre del avion
        pos = len(self.Psalidas[aux])-1
        return aterrizar(0,pos,anterior)



if __name__ == '__main__':
    serve()
