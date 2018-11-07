using System;
using Grpc.Core;
using Aeropuerto;


namespace Avion
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);

            var cliente = new Despegue.DespegueClient(channel);
            Console.WriteLine("Ingrese la ID del avion: ");
            string user = Console.ReadLine();
            Console.WriteLine("Ingrese aeropuerto de destino: ");
            String destino = Console.ReadLine();

            Resp_Des reply = cliente.enviar_despegue(new Pista_Des {IdAvion = user, NameDestino = destino});
            Console.WriteLine("print");
            Console.WriteLine("Autprizacion" + reply.AutorizacionDespegue);
            Console.WriteLine("Pista" + reply.PistaDespegue);
            Console.WriteLine("Altura" + reply.AlturaDespegue);
            Console.WriteLine("Pos" + reply.PosicionDespegue);
            Console.WriteLine("Ant" + reply.AnteriorDespegue);
            Console.WriteLine("Ip" + reply.IpDestino);
            Console.WriteLine("Id" + reply.IdAvion);

            channel.ShutdownAsync().Wait();
            Console.WriteLine("presione cualquier tecla para salir: ");
            Console.ReadKey();



          
        }
    }
}
