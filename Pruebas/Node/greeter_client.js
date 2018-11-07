/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

var PROTO_PATH = __dirname + '/../Aeropuerto.proto';

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

var Aeropuerto_proto = grpc.loadPackageDefinition(packageDefinition).Aeropuerto;

function main() {
  var client = new Aeropuerto_proto.Prueba('localhost:50051',
                                       grpc.credentials.createInsecure());
  var user;

  if (process.argv.length >= 3) {
    user = process.argv[2];
  } else {
    user = 'Cliente';
  }
  client.enviar_altura({name: user}, function(err, response) {
    console.log('Saludos:', response.flag);
  });
}

main();
