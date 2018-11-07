import grpc
import time

import Aeropuerto_pb2
import Aeropuerto_pb2_grpc

def Despegue():
    with grpc.insecure_channel('localhost:50051') as channel: #cambiar por ip+puerto
        stub = Aeropuerto_pb2_grpc.PDespegueStub(channel)
        response = stub.enviar_despegue(Aeropuerto_pb2.Pista_Des(Pista_despegue = 1, altura_despegue = 5000))
    print("La respuesta es "+ response.flagDes)


"""
message Pista_Des{
  bool autorizacion_despegue = 1;
  int32 Pista_despegue = 2;
  int32 altura_despegue = 3;
}
"""
if __name__ == '__main__':
    print("Bienvenido al Vuelo")
    aerolinea = input("[Avion] Nombre de la Aerolinea y numero de avion: ")
    aerolinea = aerolinea.strip.split(' ')
    nombre = aerolinea[1]
    peso = input("[Avion - "+nombre+"]: Peso maximo de carga [kg]: ")
    estanque = input("[Avion - "+nombre+"]: Capacidad de combustible [L]: ")
    torre = input("[Avion - "+nombre+"]: IP de torre de control inicial: ")
    partir = input("[Avion - "+nombre+"]: desea despegar [S/N]: ")

    while partir == n or partir == N:
        time.sleep(15)
        partir = input("[Avion - "+nombre+"]: desea despegar [S/N]: ")

    #pedir autorizacion
    Despegue()  
