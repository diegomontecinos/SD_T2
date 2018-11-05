from concurrent import futures
import time

import grpc

import Aeropuerto_pb2
import Aeropuerto_pb2_grpc


class Prueba(Aeropuerto_pb2_grpc.PruebaServicer):

    def enviar_altura(self, request, context):
        return Aeropuerto_pb2.respuesta(flag = "OK")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Aeropuerto_pb2_grpc.add_PruebaServicer_to_server(Prueba(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
