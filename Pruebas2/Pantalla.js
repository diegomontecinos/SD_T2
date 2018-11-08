#creo que esta hay que cambiar __dirname + [donde esta el proto]
var PROTO_PATH = __dirname + '/../../../protos/route_guide.proto';


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

var PackagePantalla = grpc.loadPackageDefinition(packageDefinition).Torre;
#llamda al codigo contructor

function main(){

  var pantalla1 = new Torre_proto.Pantalla('localhost:50051',
                            grpc.credentials.createInsecure());
  var idPantalla = "999"

  pantalla1.enviar_info({name: idPantalla}),function(err,response){
    console.log("Departures\nAvion   Destino     Pista   Hr")
    console.log(response.Salida1,'\t',response.A_Donde1,'\t',response.Pista_Salida1,'\t',response.Hora_Salida1)
    console.log(response.Salida2,'\t',response.A_Donde2,'\t',response.Pista_Salida2,'\t',response.Hora_Salida2)
    console.log("Arrivals\nAvion   Destino     Pista   Hr")
    console.log(response.Llegda1,'\t',response.De_donde1,'\t',response.Pista_Llegada1,'\t', response.Hora_Llegada1)
    console.log(response.Llegda2,'\t',response.De_donde2,'\t',response.Pista_Llegada2,'\t', response.Hora_Llegada2)
  }

}
