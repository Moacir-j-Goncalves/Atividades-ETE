import java.util.Scanner;

        // Exercicio 1

public class taref1 {

    public static void main(String[] args) {

        Scanner entrada = new 
            Scanner(System.in);

        System.out.print("Digite a sua nota: ");

        int nota = entrada.nextInt();

        if (nota >= 7) {
            System.out.println("Aprovado!");
        } else if (nota >= 5) {
            System.out.println("Recuperação.");
        } else {
            System.out.println("Reprovado.");
        }
    }
}