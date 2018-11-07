using System;
using Grpc.Core;
using Aeropuerto;


namespace Avion
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:500051", ChannelCredentials.Insecure);

            var cliente = new Despegue.DespegueClient(channel);
            String user = "Avion X";

            var reply = cliente.enviar_despegue(new Pista_Des { IdAvion = user });
            Console.WriteLine("Autprizacion" + reply.AutorizacionDespegue);

            channel.ShutdownAsync().Wait();
            Console.WriteLine("presione alguna wea");
            Console.ReadKey();



          
        }
    }
}
