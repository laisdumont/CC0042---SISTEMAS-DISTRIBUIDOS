import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class MessageServiceImpl extends UnicastRemoteObject implements MessageService {
    private List<String> messageList;

    protected MessageServiceImpl() throws RemoteException {
        super();
        messageList = new ArrayList<>();
    }

    @Override
    public void sendMessage(String message) throws RemoteException {
        messageList.add(message);
        System.out.println("Nova mensagem recebida: " + message);
    }

    @Override
    public List<String> getMessageList() throws RemoteException {
        return messageList;
    }

    @Override
    public String getServerIP() throws RemoteException {
        try {
            return java.net.InetAddress.getLocalHost().getHostAddress();
        } catch (UnknownHostException e) {
            System.err.println("Erro ao obter o IP do servidor: " + e.getMessage());
            return "IP não disponível";
        }
    }

    @Override
    public String getServerDateTime() throws RemoteException {
        return new Date().toString();
    }
}
