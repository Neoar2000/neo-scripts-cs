import java.util.ArrayList;
import java.util.Scanner;

public class Equipo {
    private ArrayList<Jugador> jugadores;
    private String nombre;
    private String carrera;
    private Jugador capitan;
    private int partidosJugados;
    private int partidosGanados;
    private int partidosPerdidos;
    private int partidosEmpatados;
    private int golesFavor;
    private int golesContra;

    // Constructor
    public Equipo(String nombre, String carrera) {
        this.nombre = nombre;
        this.carrera = carrera;
        this.jugadores = new ArrayList<>();
        this.partidosJugados = 0;
        this.partidosGanados = 0;
        this.partidosPerdidos = 0;
        this.partidosEmpatados = 0;
        this.golesFavor = 0;
        this.golesContra = 0;
    }

    // Métodos setter y getter para cada atributo
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCapitan(Jugador capitan) {
        this.capitan = capitan;
    }

    public Jugador getCapitan() {
        return capitan;
    }

    public void setPartidosJugados(int partidosJugados) {
        this.partidosJugados = partidosJugados;
    }

    public int getPartidosJugados() {
        return partidosJugados;
    }

    public void setPartidosGanados(int partidosGanados) {
        this.partidosGanados = partidosGanados;
    }

    public int getPartidosGanados() {
        return partidosGanados;
    }

    public void setPartidosPerdidos(int partidosPerdidos) {
        this.partidosPerdidos = partidosPerdidos;
    }

    public int getPartidosPerdidos() {
        return partidosPerdidos;
    }

    public void setPartidosEmpatados(int partidosEmpatados) {
        this.partidosEmpatados = partidosEmpatados;
    }

    public int getPartidosEmpatados() {
        return partidosEmpatados;
    }

    public void setGolesFavor(int golesFavor) {
        this.golesFavor = golesFavor;
    }

    public int getGolesFavor() {
        return golesFavor;
    }

    public void setGolesContra(int golesContra) {
        this.golesContra = golesContra;
    }

    public int getGolesContra() {
        return golesContra;
    }

    // Método para añadir un jugador al equipo
    public void agregarJugador(Jugador jugador) {
        Scanner lector = new Scanner(System.in);
        System.out.println("\tREGISTRO DE JUGADORES ");
        System.out.println("==============================");
        System.out.println("Ingrese el nombre del jugador: ");
        String nombre = lector.nextLine();
        System.out.println("Ingrese la posición del jugador: ");
        String posicion = lector.nextLine();
        System.out.println("Ingrese el número de casaca del jugador: ");
        int nroCasaca = lector.nextInt();
        System.out.println("Ingrese el día de nacimiento del jugador: ");
        int dia = lector.nextInt();
        System.out.println("Ingrese el mes de nacimiento del jugador: ");
        int mes = lector.nextInt();
        System.out.println("Ingrese el año de nacimiento del jugador: ");
        int anio = lector.nextInt();
        Jugador nuevoJugador = new Jugador();
        nuevoJugador.setJugador(nombre, posicion, nroCasaca, dia, mes, anio);
        jugadores.add(nuevoJugador);
        lector.close();
    }

    // Método toString para mostrar la información del equipo
    public String toString() {
        return "Nombre del equipo: " + nombre + "\nCarrera: " + carrera + "\nCapitan: " + capitan.getNombre() + "\nPartidos jugados: " + partidosJugados + "\nPartidos ganados: " + partidosGanados + "\nPartidos perdidos: " + partidosPerdidos + "\nPartidos empatados: " + partidosEmpatados + "\nGoles a favor: " + golesFavor + "\nGoles en contra: " + golesContra;
    }
}
