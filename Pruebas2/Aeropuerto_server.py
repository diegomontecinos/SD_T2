from concurrent import futures
import time

import grpc

import Aeropuerto_pb2
import Aeropuerto_pb2_grpc

print("Bienvenido a la torre de control")
nombre = input("Por favor ingrese nombre del aeropuerto: ")
IP = input("Por favor ingrese la dirección IP del aeropuerto "+nombre+": ")
pistas = input("Por favor ingrese cantidad de pistas del aeropuerto "+nombre+": ")
mas = input("¿Desea agregar destinos? [S/N] :")
destinos = dict()
#flag para pistas de Aterrizaje
#flag para pistas de Despegue
#cola de Despegue
colaDesp = list()
colaAt = list()
#cola de Aterrizaje
while mas == 'S' or mas == 's':
    nombre2 = input("ingrese sonmbre de nuevo destino: ")
    IP2 = input("Ingrese dirección IP del aeropuerto "+nombre2+": ")
    destinos[nombre2] = IP2
    mas = input("¿Desea agregar destinos? [S/N] :")


class AutorizacionDes(object):
    """docstring for Autorizacion."""
    def enviar_autorizacion_des (self, request, context):
        if leng(colaDesp) > pistas:#encolarlo y
            print(1)
        else:
            print(2)




class PDespegue(Aeropuerto_pb2_grpc.PDespegueServicer):
    def enviar_despegue(self, request, context):
        return Aeropuerto_pb2.Resp_Des(flagDes = "OK")

class PAterrizaje(Aeropuerto_pb2_grpc.PAterrizajeServicer):
    def enviar_aterrizaje(self, request,context):
        return Aeropuerto_pb2.Resp_At(flagAt = "OK")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Aeropuerto_pb2_grpc.add_PDespegueServicer_to_server(PDespegue(),server)
    server.add_insecure_port('[::]:50051')#cambiar por la ip+puerto
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    """
    print("Bienvenido a la torre de control")
    nombre = input("Por favor ingrese nombre del aeropuerto: ")
    IP = input("Por favor ingrese la dirección IP del aeropuerto "+nombre+": ")
    pistas = input("Por favor ingrese cantidad de pistas del aeropuerto "+nombre+": ")
    mas = input("¿Desea agregar destinos? [S/N] :")
    destinos = dict()
    while mas == 'S' or mas == 's':
        nombre2 = input("ingrese sonmbre de nuevo destino: ")
        IP2 = input("Ingrese dirección IP del nuevo destino: ")
        destinos[nombre2] = IP2
        mas = input("¿Desea agregar destinos? [S/N] :")
        """
    serve()

    #pedir autoizacion:  ->si: pedir pusta y altura
    #                    ->no: mostrar posición entrar loop que mantega pidiendo autorizacion
