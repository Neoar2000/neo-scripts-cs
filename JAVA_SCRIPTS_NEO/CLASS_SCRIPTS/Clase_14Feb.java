package CLASS_SCRIPTS;

import java.util.*;

public class Clase_14Feb {
    public static void main(String[] args) {
        int a[] = new int[5];
        System.out.println(a);
        Scanner lector = new Scanner(System.in);
        for (int i = 0; i < a.length; i++) {
        System.out.println("Ingrese el valor de la posicion " + (i+1));
        a[i] = lector.nextInt();
        lector.close();
        }

        for (int n:a){
            System.out.println(n);
        }
    }
}
