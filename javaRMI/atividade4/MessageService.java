import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface MessageService extends Remote {
    void sendMessage(String message) throws RemoteException;
    List<String> getMessageList() throws RemoteException;
    String getServerIP() throws RemoteException;
    String getServerDateTime() throws RemoteException;
}
