package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Biblioteca;

import java.time.LocalDate;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Biblioteca bib =  new Biblioteca();
        Scanner lector = new Scanner(System.in);
        int opcion = -1;
        while (opcion != 0) {
			System.out.println("       BIBLIOTECA UCB");
            System.out.println("===========================");
            System.out.println("1. Registrar libro");
            System.out.println("2. Registrar personas");
            System.out.println("3. Registrar préstamos");
            System.out.println("4. Buscar libro");
            System.out.println("5. Buscar personas");
            System.out.println("6. Buscar préstamos");
            System.out.println("7. Ver morosos");
            System.out.println("\n0. Salir");
            System.out.print("\nIngrese su opción: ");
            
            opcion = lector.nextInt();
            lector.nextLine(); // Limpiar el buffer de entrada
            
            switch (opcion) {
				case 1:
				 	System.out.println("\nIngrese los datos del libro:");
					System.out.print("Código: ");
					int codigoLibro = lector.nextInt();
					lector.nextLine(); // Limpiar el buffer de entrada
					System.out.print("Título: ");
					String tituloLibro = lector.nextLine();
					System.out.print("Autor: ");
					String autorLibro = lector.nextLine();

					bib.agregarLibro(codigoLibro, tituloLibro, autorLibro);
					break;
                case 2:
					System.out.println("\nIngrese los datos de la persona:");
					System.out.print("CI: ");
					String ciPersona = lector.nextLine();
					System.out.print("Nombre: ");
					String nombrePersona = lector.nextLine();
					System.out.print("Teléfono: ");
					String telefonoPersona = lector.nextLine();
					System.out.print("Correo electrónico: ");
					String correoPersona = lector.nextLine();
					
					bib.agregarPersona(ciPersona, nombrePersona, telefonoPersona, correoPersona);
					break;
                case 3:
                    System.out.println("\nIngrese los datos del préstamo:");
                    System.out.print("Código del libro: ");
                    int codigoPrestamo = lector.nextInt();
                    lector.nextLine(); // Limpiar el buffer de entrada
                    System.out.print("CI de la persona: ");
                    String ciPrestamo = lector.nextLine();
                    // Obtener el libro y la persona para el préstamo
                    Libro libroPrestamo = bib.buscarLibro(codigoPrestamo);
                    Persona personaPrestamo = bib.buscarPersona(ciPrestamo);
                    if (libroPrestamo != null && personaPrestamo != null) {
                        Prestamo nuevoPrestamo = new Prestamo(personaPrestamo, libroPrestamo, LocalDate.now().getDayOfMonth(), LocalDate.now().getMonthValue(), LocalDate.now().getYear());
                        bib.agregarPrestamo(nuevoPrestamo);
                    } else {
                        System.out.println("\nEl libro o la persona no existen.\n");
                    }
                    break;
				case 4:
					System.out.println("\nIngrese el código del libro a buscar:");
					int codigoBuscar = lector.nextInt();
					lector.nextLine(); // Limpiar el buffer de entrada
					Libro libroEncontrado = bib.buscarLibro(codigoBuscar);
					if (libroEncontrado != null) {
						System.out.println("\nLibro encontrado:\n");
						System.out.println(libroEncontrado);
					} else {
						System.out.println("\nEl libro no se encuentra en la biblioteca.\n");
					}
					break;
				case 5:
					System.out.println("\nIngrese la CI de la persona a buscar:");
					String ciBusqueda = lector.nextLine();
				
					Persona personaEncontrada = bib.buscarPersona(ciBusqueda);
					if (personaEncontrada != null) {
						System.out.println("\nPersona encontrada:\n");
						System.out.println(personaEncontrada);
					} else {
						System.out.println("\nLa persona no fue encontrada.\n");
					}
					break;
				case 6:
					System.out.println("Ingrese el código del libro del préstamo a buscar:");
					int codigoPrestamoBusqueda = lector.nextInt();
					lector.nextLine(); // Limpiar el buffer de entrada
					System.out.println("Ingrese la CI de la persona del préstamo a buscar:");
					String ciPrestamoBusqueda = lector.nextLine();
				
					Prestamo prestamoEncontrado = bib.buscarPrestamo(codigoPrestamoBusqueda, ciPrestamoBusqueda);
					if (prestamoEncontrado != null) {
						System.out.println("\nPréstamo encontrado:\n");
						System.out.println(prestamoEncontrado);
					} else {
						System.out.println("\nEl préstamo no fue encontrado.\n");
					}
					break;
				case 7:
					System.out.println("Ingrese la fecha para verificar morosos (DD MM AAAA):");
					int dia = lector.nextInt();
					int mes = lector.nextInt();
					int anio = lector.nextInt();
					
					bib.verificarPrestamos(dia, mes, anio);
					break;
                case 0:
                    System.out.println("\nGracias por utilizar el sistema de la biblioteca UCB. Hasta luego!");
                    break;
                default:
                    System.out.println("Opción no válida. Por favor, ingrese una opción válida.");
                    break;
            }
        }
        lector.close();
    }
}
