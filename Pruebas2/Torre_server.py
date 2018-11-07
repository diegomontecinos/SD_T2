# python -m grpc_tools.protoc -I"." --python_out=. --grpc_python_out=. ./Torre.proto
from concurrent import futures
import time
import random

import grpc

import Torre_pb2
import Torre_pb2_grpc

#def asignar_pista():









class Despegue(Torre_pb2_grpc.DespegueServicer):
    def __init__(self):
        print("Bienvenido a la torre de control")
        self.nombre = input("Por favor ingrese nombre del aeropuerto: ")
        self.IP = input("Por favor ingrese la dirección IP del aeropuerto "+self.nombre+": ")
        self.pistas = int(input("Por favor ingrese cantidad de pistas del aeropuerto "+self.nombre+": "))
        self.altura = 4050 #altura en metros
        self.Pentrada = dict()
        self.Pentrada["Pista 0"] = "Pista 0"
        self.Psalidas = dict()
        self.Psalidas["Pista 0"] = "Pista 0"
        for i in range(self.pistas):
            self.auxx = i+1
            self.aux2 = str(self.auxx)
            self.Pentrada["Pista ",self.aux2] = list()
            self.Psalidas["Pista ",self.aux2] = list()
        self.mas = input("¿Desea agregar destinos? [S/N] :")
        self.destinos = dict()
        #flag para pistas de Aterrizaje
        #flag para pistas de Despegue
        #cola de Despegue
        #self.colaDesp = list()
        #self.colaAt = list()
        #cola de Aterrizaje
        while self.mas == 'S' or self.mas == 's':
            self.nombre2 = input("ingrese sonmbre de nuevo destino: ")
            self.IP2 = input("Ingrese dirección IP del aeropuerto "+self.nombre2+": ")
            self.destinos[self.nombre2] = self.IP2
            self.mas = input("¿Desea agregar destinos? [S/N] :")
    @staticmethod
    def despegar(flag, pos, anterior, altura, pista):

        with grpc.insecure_channel('localhost:50051') as channel: #cambiar por ip+puerto
            stub = Torre_pb2_grpc.DespegueStub(channel)
            if flag == 0:
                response = stub.enviar_despegue(Torre_pb2.Resp_Des(Autorizacion_despegue = False, Pista_despegue = pista, Altura_despegue = altura, Posicion_despegue = pos,anterior_despegue = anterior, Ip_destino="2",Id_avion = "1"))
            else:
                response = stub.enviar_despegue(Torre_pb2.Resp_Des(Autorizacion_despegue = True, Pista_despegue = pista, Altura_despegue = altura, Posicion_despegue = pos, Anterior_despegue = anterior,Ip_destino="2",Id_avion= "1"))


    def aterrizar(flag,pos,anterior,altura,pista):
        with grpc.insecure_channel('localhost:50051') as channel: #cambiar por ip+puerto
            stub = Torre_pb2_grpc.Pista_AtgueStub(channel)
            if flag == 0:
                response = stub.enviar_aterrizaje(Torre_pb2.Pista_At(Autorizacion_aterrizaje = False, Pista_aterrizaje = pista, altura_aterrizaje = altura, posicion_aterrizaje = pos,anterior_aterrizaje = anterior))
            else:
                response = stub.enviar_aterrizaje(Torre_pb2.Pista_At(autorizacion_aterrizaje = True, Pista_aterrizaje = pista, altura_aterrizaje = altura, posicion_aterrizaje = pos,anterior_aterrizaje = anterior))

    def enviar_despegue (self, request, context):
        return (self.despegar(1, 0, 'nadie', 0, 1))
        """for i in range(self.pistas):
            if len(self.Pentrada["Pista ",str(i+1)])<self.pistas:
                #if() revisar si está en esa lista y sacarlo de ahúí
                #sacarlo de la cola
                self.altura = self.altura + 50
                return despegar(1,-1,"nadie",self.altura,self.Pentrada["Pista 0"])
                #break
        #anterior = colaDesp[-1] ver bien como ver el anterior
        aux = self.Pentrada["Pista 0"]

        self.Pentrada[aux].append(self.nombre)#es el nombre del avion
        pos = len(self.Pentrada[aux])-1
        return despegar(0,pos,anterior,0,aux)
        """

    def enviar_aterrizaje (self, request, context):
        for i in range(self.pistas):
            if len(self.Psalidas["Pista "+str(i+1)])<self.pistas:
                #ver si está en esa cola y sacarlo
                self.altura = self.altura + 50
                return aterrizar(1,(i+1),"nadie",self.altura,self.Psalidas["Pista 0"])

        self.altura +=50
        aux = self.Psalidas["Pista 0"]
        self.Psalidas[aux].append() #nombre del avion
        pos = len(self.Psalidas[aux])-1
        return aterrizar(0,pos,anterior,self.altura,aux)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Torre_pb2_grpc.add_DespegueServicer_to_server(Despegue(),server)
    server.add_insecure_port('[::]:50051')#cambiar por la ip+puerto
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
