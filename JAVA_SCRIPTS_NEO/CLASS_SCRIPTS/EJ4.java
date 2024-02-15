package CLASS_SCRIPTS;

import java.util.*;

public class EJ4 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sumatoriaPrimos = 0;

        while (true) {
            System.out.print("Ingrese un número entero (0 para terminar): ");
            int numero = scanner.nextInt();

            if (numero == 0) {
                break;
            }

            if (esPrimo(numero)) {
                sumatoriaPrimos += numero;
            }
        }

        System.out.println("La sumatoria de todos los números primos introducidos es: " + sumatoriaPrimos);

        scanner.close();
    }

    public static boolean esPrimo(int numero) {
        if (numero <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(numero); i++) {
            if (numero % i == 0) {
                return false;
            }
        }
        return true;
    }
}