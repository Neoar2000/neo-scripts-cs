package CLASS_SCRIPTS;

import java.util.*;

public class RegistroEstudiantes {
    public static void main(String[] args) {
        ArrayList<String> nombres = new ArrayList<>();
        ArrayList<Integer> notaPrimerParcial = new ArrayList<>();
        ArrayList<Integer> notaSegundoParcial = new ArrayList<>();
        
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            clearConsole();
            System.out.println("\t   SISTEMA DE REGISTRO ESTUDIANTIL");
            System.out.println("====================================================");
            System.out.println("1. Añadir estudiante");
            System.out.println("2. Mostrar Lista de Estudiantes");
            System.out.println("3. Calcular nota de habilitación");
            System.out.println("4. Mostrar lista de notas");
            System.out.println("5. Mostrar la lista de los estudiantes habilitados");
            System.out.println("6. Salir");
            System.out.print("\nSeleccione una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    // Añadir estudiante
                    clearConsole();
                    scanner.nextLine(); // Limpiar el buffer del scanner
                    System.out.print("Ingrese apellidos y nombres del estudiante: ");
                    String nombre = scanner.nextLine();
                    nombres.add(nombre);

                    System.out.print("Ingrese nota del primer parcial (sobre 100): ");
                    int nota1 = scanner.nextInt();
                    notaPrimerParcial.add(nota1);

                    System.out.print("Ingrese nota del segundo parcial (sobre 100): ");
                    int nota2 = scanner.nextInt();
                    notaSegundoParcial.add(nota2);
                    break;

                case 2:
                    // Mostrar Lista de Estudiantes
                    clearConsole();
                    mostrarListaEstudiantes(nombres);
                    esperarTecla();
                    break;

                case 3:
                    // Calcular nota de habilitación
                    clearConsole();
                    calcularNotaHabilitacion(notaPrimerParcial, notaSegundoParcial);
                    esperarTecla();
                    break;

                case 4:
                    // Mostrar lista de notas
                    clearConsole();
                    mostrarListaNotas(nombres, notaPrimerParcial, notaSegundoParcial);
                    esperarTecla();
                    break;

                case 5:
                    // Mostrar la lista de los estudiantes habilitados
                    clearConsole();
                    mostrarEstudiantesHabilitados(nombres, notaPrimerParcial, notaSegundoParcial);
                    esperarTecla();
                    break;

                case 6:
                    // Salir
                    clearConsole();
                    System.out.println("Gracias por usar el sistema de registro estudiantil. Hasta luego!");
                    break;

                default:
                    clearConsole();
                    System.out.println("Opción inválida. Por favor, seleccione una opción del 1 al 6.");
                    esperarTecla();
            }

        } while (opcion != 6);

        scanner.close();
    }

    // Método para mostrar la lista de estudiantes
    public static void mostrarListaEstudiantes(ArrayList<String> nombres) {
        Collections.sort(nombres);
        System.out.println("Lista de Estudiantes:");
        for (String nombre : nombres) {
            System.out.println(nombre);
        }
    }

    // Método para calcular la nota de habilitación
    public static void calcularNotaHabilitacion(ArrayList<Integer> notaPrimerParcial, ArrayList<Integer> notaSegundoParcial) {
        ArrayList<Double> notaHabilitacion = new ArrayList<>();
        for (int i = 0; i < notaPrimerParcial.size(); i++) {
            double promedio = (notaPrimerParcial.get(i) + notaSegundoParcial.get(i)) / 2.0;
            notaHabilitacion.add(promedio);
        }
        System.out.println("Notas de habilitación calculadas.");
    }    

    // Método para mostrar la lista de notas
    public static void mostrarListaNotas(ArrayList<String> nombres, ArrayList<Integer> notaPrimerParcial, ArrayList<Integer> notaSegundoParcial) {
        System.out.println("Lista de Notas:");
        for (int i = 0; i < nombres.size(); i++) {
            System.out.println("Estudiante: " + nombres.get(i) + ", 1er Parcial: " + notaPrimerParcial.get(i) + ", 2do Parcial: " + notaSegundoParcial.get(i));
        }
    }

    // Método para mostrar la lista de estudiantes habilitados
    public static void mostrarEstudiantesHabilitados(ArrayList<String> nombres, ArrayList<Integer> notaPrimerParcial, ArrayList<Integer> notaSegundoParcial) {
        // Eliminar estudiantes no habilitados
        ArrayList<String> estudiantesHabilitados = new ArrayList<>();
        for (int i = 0; i < nombres.size(); i++) {
            double promedio = (notaPrimerParcial.get(i) + notaSegundoParcial.get(i)) / 2.0;
            if (promedio >= 60) {
                estudiantesHabilitados.add(nombres.get(i));
            }
        }

        // Mostrar estudiantes habilitados
        System.out.println("Estudiantes habilitados:");
        for (String nombre : estudiantesHabilitados) {
            System.out.println(nombre);
        }

        // Comprobar eximisión
        boolean eximision = false;
        for (int i = 0; i < notaPrimerParcial.size(); i++) {
            if (notaPrimerParcial.get(i) > 95 || notaSegundoParcial.get(i) > 95) {
                eximision = true;
                break;
            }
        }

        if (eximision) {
            System.out.println("Hay estudiantes con posibilidad de eximisión");
        }
    }

    public static void esperarTecla() {
        System.out.println("\nPresione cualquier tecla para continuar...");
        try {
            System.in.read();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static void clearConsole() {
        try {
            final String os = System.getProperty("os.name");
            if (os.contains("Windows")) {
                // Si el sistema operativo es Windows
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                // Si es otro sistema operativo (Unix, Linux, macOS)
                Runtime.getRuntime().exec("clear");
            }
        } catch (final Exception e) {
            // Manejo de excepciones
            System.out.println("Error al limpiar la consola: " + e.getMessage());
        }
    }
}
