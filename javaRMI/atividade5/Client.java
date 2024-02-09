import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            // Procurando o serviço remoto
            CurrencyConverter currencyConverter = (CurrencyConverter) Naming.lookup("//localhost/CurrencyConverter");

            // Realizando conversões
            double euro = 100;
            double real = 200;
            double dollar = 50;

            double euroToRealResult = currencyConverter.euroToReal(euro);
            double realToEuroResult = currencyConverter.realToEuro(real);
            double dollarToRealResult = currencyConverter.dollarToReal(dollar);
            double realToDollarResult = currencyConverter.realToDollar(real);

            System.out.println("Conversão de Euro para Real: " + euroToRealResult);
            System.out.println("Conversão de Real para Euro: " + realToEuroResult);
            System.out.println("Conversão de Dólar para Real: " + dollarToRealResult);
            System.out.println("Conversão de Real para Dólar: " + realToDollarResult);

        } catch (Exception e) {
            System.err.println("Erro no cliente: " + e.toString());
            e.printStackTrace();
        }
    }
}
