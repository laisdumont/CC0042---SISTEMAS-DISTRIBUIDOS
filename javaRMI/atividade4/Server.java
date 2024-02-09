import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // Iniciando o registro do RMI
            LocateRegistry.createRegistry(1099);

            // Criando uma instância do serviço
            MessageService messageService = new MessageServiceImpl();

            // Publicando o serviço
            Naming.rebind("//localhost/MessageService", messageService);

            System.out.println("Servidor pronto...");

        } catch (Exception e) {
            System.err.println("Erro no servidor: " + e.toString());
            e.printStackTrace();
        }
    }
}
