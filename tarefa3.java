
import java.util.Scanner;

public class tarefa3 {
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
