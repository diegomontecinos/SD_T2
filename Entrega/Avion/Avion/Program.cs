using System;
using Grpc.Core;
using Aeropuerto;


namespace Avion
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string Ip_torre_despegue = "127.0.0.1";
            Console.WriteLine("Ingrese Ip de la torre de control, si ingresa el valor 0 se utilizara la IP por defecto 127.0.0.1 para conecciones avion-torre en el mismo equipo: ");
            string temp = Console.ReadLine();

            if (temp != "0")
            {
                Ip_torre_despegue = temp;
            }

            Channel channel = new Channel(string.Concat(Ip_torre_despegue,":50051"), ChannelCredentials.Insecure);
            //crear una variable de objeto cliente - guarda las respuestas
            var cliente = new Serv_Aeropuerto.Serv_AeropuertoClient(channel);

            Console.WriteLine("Ingrese la ID del avion: ");
            string user = Console.ReadLine();
            Console.WriteLine("Ingrese aeropuerto de destino: ");
            String destino = Console.ReadLine();

            var reply = cliente.enviar_despegue(new Pista_Des {IdAvion = user, NameDestino = destino});
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
