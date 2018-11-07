import grpc
import time

import Torre_pb2
import Torre_pb2_grpc

def Despegue():
    with grpc.insecure_channel('localhost:50051') as channel: #cambiar por ip+puerto
        stub = Torre_pb2_grpc.PDespegueStub(channel)
        response = stub.enviar_despegue(Torre_pb2.Pista_Des(autorizacion_despegue = True, Pista_despegue = 1, altura_despegue = 5000, posicion_despegue = 3, anterior_despegue = "alguien"))
    print("La respuesta es "+ response.flagDes)


"""
message Pista_Des{
  bool autorizacion_despegue = 1;
  int32 Pista_despegue = 2;
  int32 altura_despegue = 3;
  int32 posicion_despegue = 4;
  string anterior_despegue = 5;
}
"""
if __name__ == '__main__':
    print("Bienvenido al Vuelo")
    aerolinea = input("[Avion] Nombre de la Aerolinea y numero de avion: ")
    aerolinea = aerolinea.strip().split( )
    print(aerolinea)
    nombre = aerolinea[1]
    peso = int(input("[Avion - "+nombre+"]: Peso maximo de carga [kg]: "))
    estanque = int(input("[Avion - "+nombre+"]: Capacidad de combustible [L]: "))
    torre = input("[Avion - "+nombre+"]: IP de torre de control inicial: ")
    partir = input("[Avion - "+nombre+"]: desea despegar [S/N]: ")

    while partir == 'n' or partir == 'N':
        time.sleep(15)
        partir = input("[Avion - "+nombre+"]: desea despegar [S/N]: ")

    #pedir autorizacion
    Despegue()
