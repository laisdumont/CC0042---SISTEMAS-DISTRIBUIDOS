import java.rmi.Naming;
import java.util.List;

public class Client {
    public static void main(String[] args) {
        try {
            // Procurando o serviço remoto
            MessageService messageService = (MessageService) Naming.lookup("//localhost/MessageService");

            // Enviando uma mensagem para o servidor
            messageService.sendMessage("Bem vindo!");

            // Recuperando a lista de mensagens do servidor
            List<String> messages = messageService.getMessageList();
            System.out.println("Mensagens no servidor:");
            for (String message : messages) {
                System.out.println("- " + message);
            }

            // Recuperando o IP do servidor
            String serverIP = messageService.getServerIP();
            System.out.println("IP do servidor: " + serverIP);

            // Recuperando a data e hora do servidor
            String serverDateTime = messageService.getServerDateTime();
            System.out.println("Data e hora do servidor: " + serverDateTime);

        } catch (Exception e) {
            System.err.println("Erro no cliente: " + e.toString());
            e.printStackTrace();
        }
    }
}
