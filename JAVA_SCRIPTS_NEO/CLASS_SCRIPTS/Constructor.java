package CLASS_SCRIPTS;

public class Constructor {
    public static void main(String[] args) {
        Rectangulo r1 = new Rectangulo(5.2, 10.5, "Rojo");
        clearConsole();
        System.out.println(r1.getBase());
        System.out.println(r1.getAltura());
        System.out.println(r1.getColor());
    }

    public static void clearConsole() {
        try {
            final String os = System.getProperty("os.name");
            if (os.contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        } catch (final Exception e) {
            System.out.println("Error al limpiar la consola: " + e.getMessage());
        }
    }
}