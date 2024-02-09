import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CurrencyConverterImpl extends UnicastRemoteObject implements CurrencyConverter {
    protected CurrencyConverterImpl() throws RemoteException {
        super();
    }

    @Override
    public double euroToReal(double euro) throws RemoteException {
        // Valor do euro em reais (cotação atual 9 de fev., 16:32 UTC)
        double euroToRealRate = 5.36;
        return euro * euroToRealRate;
    }

    @Override
    public double realToEuro(double real) throws RemoteException {
        // Valor do real em euros (cotação atual 9 de fev., 16:32 UTC)
        double realToEuroRate = 0.19;
        return real * realToEuroRate;
    }

    @Override
    public double dollarToReal(double dollar) throws RemoteException {
        // Valor do dólar em reais (cotação atual 9 de fev., 16:32 UTC)
        double dollarToRealRate = 4.97;
        return dollar * dollarToRealRate;
    }

    @Override
    public double realToDollar(double real) throws RemoteException {
        // Valor do real em dólares (cotação atual 9 de fev., 16:32 UTC)
        double realToDollarRate = 0.20;
        return real * realToDollarRate;
    }
}
