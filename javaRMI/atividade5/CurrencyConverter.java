import java.rmi.Remote;
import java.rmi.RemoteException;

public interface CurrencyConverter extends Remote {
    double euroToReal(double euro) throws RemoteException;
    double realToEuro(double real) throws RemoteException;
    double dollarToReal(double dollar) throws RemoteException;
    double realToDollar(double real) throws RemoteException;
}
