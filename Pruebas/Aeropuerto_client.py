#from __future__ import print_function
import grpc

import Aeropuerto_pb2
import Aeropuerto_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Aeropuerto_pb2_grpc.PruebaStub(channel)
        response = stub.enviar_altura(Aeropuerto_pb2.mensaje(altura = 50))
    print("La respuesta es" + response.flag)


if __name__ == '__main__':
    run()
