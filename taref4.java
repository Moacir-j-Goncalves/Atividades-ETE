import java.util.Scanner;

public class taref4 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite seu Nome: ");
        String Nome = teclado.nextLine();

        System.out.println("Digite seu Sobrenome: ");
        String Sobrenome = teclado.nextLine();

        System.out.println("Digite sua Idade: ");
        String Idade = teclado.nextLine();

        System.out.println("Digite seu Peso: ");
        String Peso = teclado.nextLine();

        System.out.println(
                "Óla " + Nome + " " + Sobrenome + "! " + "você tem " + Idade + " anos " + "e seu peso é " + Peso + ".");

    }

}
