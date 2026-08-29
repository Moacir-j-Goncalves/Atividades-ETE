public class Tarefa2 {

    public static void main(String[] args) {

        double nota1 = 8.0;
        double nota2 = 6.0;
        double nota3 = 7.0;

        double media = (nota1 + nota2 + nota3) / 3;

        if (media >= 7) {
            System.out.println("Aprovado");
        } else if (media >= 5) {
            System.out.println("Recuperação");
        } else {
            System.out.println("Reprovado");
        }

        System.out.println("Média: " + media);
    }
}