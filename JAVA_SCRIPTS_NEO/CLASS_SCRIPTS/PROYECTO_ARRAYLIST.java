package CLASS_SCRIPTS;

import java.util.*;

public class PROYECTO_ARRAYLIST {
    public static void main(String[] args) {
        char [][] tablero = new char [8][8];
        llenartablero(tablero);
        mostrarTablero(tablero);
        Scanner lector = new Scanner(System.in);

        //Solicitar la posición del rey blanco al usuario
        System.out.println("Ingrese la posición del rey blanco");
        String posRey = lector.nextLine();
        int filaRey = 8-(posRey.charAt(2)-48);
        int colRey = posRey.charAt(1)-97;
        tablero[filaRey][colRey] = posRey.charAt(0);
        mostrarTablero(tablero);
    
        //Solicitar piezas negras
        ArrayList<String> piezasNegras = new ArrayList<String>();
        System.out.println("Numero de piezas negras");
        int nPiezas = lector.nextInt();
        for (int i = 0; i < nPiezas; i++) {
            System.out.println("Ingrese la posicion " + (i+1));
            String p = lector.next();
            piezasNegras.add(p);
        }

        //Ubicar piezas en el tablero
        for (String pieza : piezasNegras) {
            int fila = 8-(pieza.charAt(2)-48);
            int col = pieza.charAt(1)-97;
            tablero[fila][col] = pieza.charAt(0);
        }

        mostrarTablero(tablero);
        lector.close();

    }

    public static void llenartablero(char[][] tablero) {
        //Llenar el tablero con espacios
        for (int i = 0; i < tablero.length; i++) {
            for (int j = 0; j < tablero[0].length; j++) {
                tablero[i][j] = '0';
            }
        }
    }

    public static void mostrarTablero(char[][] tablero) {
        System.out.println("  a b c d e f g h");
        for (int i = 0; i < tablero.length; i++) {
            System.out.print((8-i) + " ");
            for (int j = 0; j < tablero[0].length; j++) {
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
    }
}