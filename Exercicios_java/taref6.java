import java.util.Scanner;

public class taref6 {
    public static void main(String[] args) {
        double  K, F, Re, Ra;


            Scanner teclado = new Scanner(System.in);

        System.out.println("Digite a temperatura em Celsius: ");
                double Temp = teclado.nextDouble();

        
        K = Temp + 273.15;
        F = Temp * 1.8 +32;
        Re = Temp * 1.8 + 32 + 459.67;
        Ra = Temp* 0.8;

        System.out.println("A temperatua em fahrenheit é: " + F);
        System.out.println("A temperatua em Kelvin é: " + K);
        System.out.println("A temperatua em Reamur é: "+ Ra);
        System.out.println("A temperatua em Rankine é: "+ Re);

    }
}



