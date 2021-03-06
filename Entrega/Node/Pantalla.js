//creo que esta hay que cambiar __dirname + [donde esta el proto]
var PROTO_PATH = __dirname + '/../Protos/Torre.proto';


var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

var packagePantalla = grpc.loadPackageDefinition(packageDefinition).Aeropuerto;

function main(){

  console.log("Ingrese IP del aeropuerto, si la torre esta en el mismo equipo, por favor escriba: localhost");
  //pide la ip de la torre
  var ipTorreAux = process.openStdin();

  //stdin.addListener("data", function(d) {
  //    console.log("Tu nombre es: " +
  //        d.toString().trim());
  //  });

  //junta ip+puerto
  var puerto = ":50051";
  ipPuerto = ipTorreAux+puerto;
  //console.log(ipPuerto);

  var pantalla1 = new packagePantalla.Serv_Aeropuerto('localhost:50051',//ipPuerto,
                            grpc.credentials.createInsecure());


  //pide id para cada pantalla
  console.log("Ingrese ID de Pantalla");
  var idPantalla = process.openStdin();

  //pedimos y mostramos info

  pantalla1.enviar_info({Nombre_Pantalla: idPantalla},function(err,response){
    console.log("Departures\nAvion\tDestino\tPista\tHr");
    console.log(response.Salida1,'\t',response.A_Donde1,'\t',response.Pista_Salida1,'\t',response.Hora_Salida1);
    console.log(response.Salida2,'\t',response.A_Donde2,'\t',response.Pista_Salida2,'\t',response.Hora_Salida2);
    console.log("Arrivals\nAvion   Destino     Pista   Hr");
    console.log(response.Llegda1,'\t',response.De_donde1,'\t',response.Pista_Llegada1,'\t', response.Hora_Llegada1);
    console.log(response.Llegda2,'\t',response.De_donde2,'\t',response.Pista_Llegada2,'\t', response.Hora_Llegada2);
  });

//  var cliente = new services.Serv_AeropuertoClient(ipPuerto,
//                            grpc.credentials.createInsecure());
//  var requuest = new messages.Id_Pantalla();
//  request.setName(idPantalla);
//  client.enviar_info(request,function(err, response){
//    console.log("Departures\nAvion   Destino     Pista   Hr");
//    console.log("a",response.Salida1,'\t',response.A_Donde1,'\t',response.Pista_Salida1,'\t',response.Hora_Salida1);
//    console.log(response.Salida2,'\t',response.A_Donde2,'\t',response.Pista_Salida2,'\t',response.Hora_Salida2);
//    console.log("Arrivals\nAvion   Destino     Pista   Hr");
//    console.log(response.Llegda1,'\t',response.De_donde1,'\t',response.Pista_Llegada1,'\t', response.Hora_Llegada1);
//    console.log(response.Llegda2,'\t',response.De_donde2,'\t',response.Pista_Llegada2,'\t', response.Hora_Llegada2);
//  });


}

main();
