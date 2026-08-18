import java.util.Scanner;

public class time {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = teclado.nextLine();

        System.out.print("Digite seu sobrenome: ");
        String sobrenome = teclado.nextLine();

        System.out.print("Digite sua data de nascimento: ");
        String dataNascimento = teclado.nextLine();

        System.out.print("Digite seu time de coração: ");
        String time = teclado.nextLine();

        System.out.println();

        System.out.println("Seu nome é " + nome + " " + sobrenome);
        System.out.println("Seu time de coração é " + time
                + " e sua data de nascimento é " + dataNascimento);

        teclado.close();
    }
}