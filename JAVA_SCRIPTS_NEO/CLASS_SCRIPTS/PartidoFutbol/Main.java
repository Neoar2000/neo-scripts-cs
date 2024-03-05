public class Main {
    public static void main(String[] args) {
        // Crear instancia de Jugador
        Jugador jugador = new Jugador();
        jugador.setJugador("Neo Aliaga", "Central", 6, 1, 1, 2000);

        // Crear instancia de Partido
        Partido partido = new Partido();
        partido.setPartido("Equipo A", "Equipo B", 2, 1, 5, 3, 2024, "Estadio XYZ", 18, 0, 20, 0);

        // Mostrar información del jugador
        System.out.println("Información del Jugador:");
        System.out.println(jugador.toString());
        System.out.println();

        // Mostrar información del partido
        System.out.println("Información del Partido:");
        System.out.println(partido.toString());
        System.out.println();

        // Crear instancia de Equipo
        Equipo equipo = new Equipo("Equipo de prueba", "Informática");

        // Agregar jugador al equipo
        equipo.agregarJugador(jugador);

        // Asignar un capitán al equipo
        equipo.setCapitan(jugador);

        // Mostrar información del equipo
        System.out.println("Información del Equipo:");
        System.out.println(equipo.toString());
    }
}
