package CLASS_SCRIPTS;

import java.util.*;

public class EJ3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el primer número: ");
        int numero1 = scanner.nextInt();

        System.out.print("Ingrese el segundo número: ");
        int numero2 = scanner.nextInt();

        int mcd = calcularMCD(numero1, numero2);

        System.out.println("El máximo común divisor de " + numero1 + " y " + numero2 + " es: " + mcd);

        scanner.close();
    }

    public static int calcularMCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return calcularMCD(b, a % b);
    }
}
