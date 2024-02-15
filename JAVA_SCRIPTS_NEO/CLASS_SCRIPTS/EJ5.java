package CLASS_SCRIPTS;

import java.util.*;
public class EJ5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner lector = new Scanner(System.in);
		String [][] tablero = new String [8][8];
		llenarTablero(tablero);
		
		System.out.println("Ingrese la posicion del Rey");
		String posRey = lector.next();
		int filaRey = posRey.charAt(2);
		filaRey = 7-(filaRey - 49);
		int colRey = posRey.charAt(1); 
		colRey = colRey-97;
		tablero[filaRey][colRey] = "R";
		mostrarTablero(tablero);
		
		
		lector.close();
	}
	
	public static void llenarTablero(String [][] tab) {
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				tab[i][j] = "0";
			}
		}
	}
	
	public static void mostrarTablero(String [][] tab) {
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				System.out.print(tab[i][j]+ "\t");
			}
			System.out.println();
		}
	}

}