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

            Console.WriteLine("Pasando por el Gate");
            System.Threading.Thread.Sleep(3000);
            Console.WriteLine("Todos los pasajeros a bordo y combustible cargado.");
            System.Threading.Thread.Sleep(2000);
            Console.WriteLine("Pidiendo indicaciones para despegar.");

            var reply = cliente.enviar_despegue(new Pista_Des {IdAvion = user, NameDestino = destino});

            Console.WriteLine("Autorizacion: " + reply.AutorizacionDespegue);
            Console.WriteLine("Pista: " + reply.PistaDespegue);
            Console.WriteLine("Altura: " + reply.AlturaDespegue);
            Console.WriteLine("Pos: " + reply.PosicionDespegue);
            Console.WriteLine("Ant: " + reply.AnteriorDespegue);
            Console.WriteLine("Ip: " + reply.IpDestino);
            Console.WriteLine("Id: " + reply.IdAvion);

            System.Threading.Thread.Sleep(2000);

            Resp_Cons second_reply = null;

            if (reply.AutorizacionDespegue == true)
            {
                Console.WriteLine("despegando de la pista {0},  volando a una altura de {1},", reply.PistaDespegue, reply.AlturaDespegue);
            }

            else
            {
                Console.WriteLine("Lamenatamos informar que todas las pistas se encuentran ocupadas, salremos luego del avion {0}, hay {1} aviones antes nuestro.", reply.AnteriorDespegue, reply.PosicionDespegue);
                second_reply = cliente.confirmar_despegue(new Cons_Des { IdAvion = user, NameDestino = destino, PistaEspera = reply.PistaDespegue, PosicionEspera = reply.PosicionDespegue });

                string Pista_espera = second_reply.PistaDespegue;

                if (second_reply.AutorizacionDespegue == true)
                {
                    Console.WriteLine("despegando de la pista {0},  volando a una altura de {1},", second_reply.PistaDespegue, second_reply.AlturaDespegue);
                }

                else
                {

                    while (second_reply.AutorizacionDespegue == false)
                    {
                        second_reply = cliente.confirmar_despegue(new Cons_Des { IdAvion = user, NameDestino = destino, PistaEspera = Pista_espera});


                        if (second_reply.AutorizacionDespegue == true)
                        {
                            Console.WriteLine("Aun hay {0} aviones esperando para despegar.", second_reply.PosicionDespegue);
                        }
                        else
                        {
                            Console.WriteLine("Procederemos a despegar.");
                        }
                    }
                }

                Console.WriteLine("Autorizacion: {0} ", second_reply.AutorizacionDespegue);
                Console.WriteLine("Pista: " + second_reply.PistaDespegue);
                Console.WriteLine("Altura: " + second_reply.AlturaDespegue);
                Console.WriteLine("Pos: " + second_reply.PosicionDespegue);
                Console.WriteLine("Ant: " + second_reply.AnteriorDespegue);
                Console.WriteLine("Ip: " + second_reply.IpDestino);
                Console.WriteLine("Id: " + second_reply.IdAvion);
            }



            channel.ShutdownAsync().Wait();
            Console.WriteLine("presione cualquier tecla para salir: ");
            Console.ReadKey();



          
        }
    }
}
