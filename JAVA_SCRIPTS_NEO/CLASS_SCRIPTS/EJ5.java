package CLASS_SCRIPTS;

import java.util.*;

public class EJ5 {

    public static void main(String[] args) {
        Scanner lector = new Scanner(System.in);
        String[][] tablero = new String[8][8];
        llenarTablero(tablero);

        System.out.println("Ingrese la posicion del Rey Blanco (ejemplo: Rf1):");
        String posRey = lector.next();
        colocarPieza(tablero, posRey, "R");

        System.out.println("Ingrese las posiciones de las piezas negras (ejemplo: a8,b7...):");
        String piezasNegras = lector.next();
        String[] posicionesNegras = piezasNegras.split(",");
        for (String posicionNegra : posicionesNegras) {
            colocarPieza(tablero, posicionNegra, obtenerNombrePieza(posicionNegra));
        }

        mostrarTablero(tablero);
        verificarJaque(tablero);
    }

    public static void llenarTablero(String[][] tab) {
        for (int i = 0; i < 8; i++) {
            Arrays.fill(tab[i], ".");
        }
    }

    public static void mostrarTablero(String[][] tab) {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                System.out.print(tab[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public static void colocarPieza(String[][] tablero, String posicion, String pieza) {
        int fila = 8 - Character.getNumericValue(posicion.charAt(1));
        int columna = posicion.charAt(0) - 'a';
        tablero[fila][columna] = pieza;
    }

    public static String obtenerNombrePieza(String posicion) {
        // Aquí puedes expandir la lógica para asignar el nombre correcto según la posición o el input
        // Por ejemplo, si el input fuera "Pa2", entonces deberías devolver "P" para el peón.
        return posicion.substring(0, 1);
    }

    public static void verificarJaque(String[][] tablero) {
        // Esta función debería implementar la lógica para determinar si el rey está en jaque.
        // Como es una lógica compleja y depende de las reglas del ajedrez, la dejaré como pendiente.
        System.out.println("Verificar si el rey está en jaque no está implementado aún.");
    }

    // ... Puedes añadir más métodos aquí si es necesario.

}