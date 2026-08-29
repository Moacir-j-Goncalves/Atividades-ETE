// Exercicio 1
// import java.util.Scanner;

// public class taref {

//     public static void main(String[] args) {

//         Scanner entrada = new 
//     Scanner(System.in);

//         System.out.print("Digite a sua nota: ");

//         int nota = entrada.nextInt();

//         if (nota >= 7) {
//             System.out.println("Aprovado!");
//         } else if (nota >= 5) {
//             System.out.println("Recuperação.");
//         } else {
//             System.out.println("Reprovado.");
//         }
//     }
// }

// Exercicio 2

// public class taref {

//     public static void main(String[] args) {

//         double nota1 = 8.0;
//         double nota2 = 6.0;
//         double nota3 = 7.0;

//         double media = (nota1 + nota2 + nota3) / 3;

//         if (media >= 7) {
//             System.out.println("Aprovado");
//         } else if (media >= 5) {
//             System.out.println("Recuperação");
//         } else {
//             System.out.println("Reprovado");
//         }

//         System.out.println("Média: " + media);
//     }
// }

// Exercicio 3

import java.util.Scanner;

public class taref {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite o valor da compra: R$ ");
        double valorcompra = sc.nextDouble();

        double desconto = 0;
        if (valorcompra < 200) {
            desconto = 0;
        } else if (valorcompra <= 300) {
            desconto = valorcompra * 0.10;

        } else {
            desconto = valorcompra * 0.20;
        }

        double valorfinal = valorcompra - desconto;

        System.out.println("valor Original: R$ " + valorcompra);
        System.out.println("Desconto: R$ " + valorfinal);

        sc.close();

    }
}

// Exercicio 4
