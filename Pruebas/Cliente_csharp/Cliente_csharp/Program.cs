using System;
using Grpc.Core;
using Aeropuerto;

namespace PruebaClient
{
    class Program
    {
        public static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);

            var client = new Prueba.PruebaClient(channel);
            String user = "cliente";

            var reply = client.enviar_altura(new mensaje { Altura = 55 });
            Console.WriteLine("Greeting: " + reply.Flag);

            channel.ShutdownAsync().Wait();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}