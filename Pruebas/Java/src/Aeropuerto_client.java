
//import grpc.StatusRuntimeException;
//import grpc.ManagedChannelBuilder;
//import grpc.ManagedChannel;

import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

import groc.*;
import proto_to_java.Aeropuerto.*;

/**
 * A simple client that requests a greeting from the {@link HelloWorldServer}.
 */
public class AeropuertoClient {
    private static final Logger logger = Logger.getLogger(AeropuertoClient.class.getName());

    private final ManagedChannel channel;
    private final PruebaGrpc.PruebaBlockingStub blockingStub;

    /** Construct client connecting to HelloWorld server at {@code host:port}. */
    public AeropuertoClient(String host, int port) {
        this(ManagedChannelBuilder.forAddress(host, port)
                // Channels are secure by default (via SSL/TLS). For the example we disable TLS to avoid
                // needing certificates.
                .usePlaintext()
                .build());
    }

    /** Construct client for accessing HelloWorld server using the existing channel. */
    AeropuertoClient(ManagedChannel channel) {
        this.channel = channel;
        blockingStub = GreeterGrpc.newBlockingStub(channel);
    }

    public void shutdown() throws InterruptedException {
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

    /** Say hello to server. */
    public void saludo(String name) {
        logger.info("tratando de saludar a  " + name + " ...");
        mensaje request = mensajeRequest.newBuilder().setName(name).build();
        respuesta response;

        try {
            response = blockingStub.enviar_altura(request);
        } catch (StatusRuntimeException e) {
            logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
            return;
        }
        logger.info("Greeting: " + response.getMessage());
    }

    /**
     * Greet server. If provided, the first element of {@code args} is the name to use in the
     * greeting.
     */
    public static void main(String[] args) throws Exception {
        AeropuertoClient client = new AeropuertoClient("localhost", 50051);
        try {
            /* Access a service running on the local machine on port 50051 */
            String user = "OK";
            if (args.length > 0) {
                user = args[0]; /* Use the arg as the name to greet if provided */
            }
            client.greet(user);
        } finally {
            client.shutdown();
        }
    }
}
