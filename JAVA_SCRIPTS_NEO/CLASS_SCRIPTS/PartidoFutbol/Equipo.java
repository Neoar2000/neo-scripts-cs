import java.util.ArrayList;

public class Equipo {
    private String carrera;
    private ArrayList<Jugador> jugadores;
    private String capitan;
    private int pJugados;
    private int pGanados;
    private int pPerdidos;
    private int pEmpatados;
    private int gFavor;
    private int gContra;

    public Equipo(String carrera, String capitan) {
        this.carrera = carrera;
        this.jugadores = new ArrayList<>();
        this.capitan = capitan;
        this.pJugados = 0;
        this.pGanados = 0;
        this.pPerdidos = 0;
        this.pEmpatados = 0;
        this.gFavor = 0;
        this.gContra = 0;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    public void verJugadores() {
        for (Jugador jugador : jugadores) {
            System.out.println(jugador.toString());
        }
    }

    public String getCapitan() {
        return capitan;
    }

    public void setCapitan(String capitan) {
        this.capitan = capitan;
    }

    public int getpJugados() {
        return pJugados;
    }

    public void setpJugados(int pJugados) {
        this.pJugados = pJugados;
    }

    public int getpGanados() {
        return pGanados;
    }

    public void setpGanados(int pGanados) {
        this.pGanados = pGanados;
    }

    public int getpPerdidos() {
        return pPerdidos;
    }

    public void setpPerdidos(int pPerdidos) {
        this.pPerdidos = pPerdidos;
    }

    public int getpEmpatados() {
        return pEmpatados;
    }

    public void setpEmpatados(int pEmpatados) {
        this.pEmpatados = pEmpatados;
    }

    public int getgFavor() {
        return gFavor;
    }

    public void setgFavor(int gFavor) {
        this.gFavor = gFavor;
    }

    public int getgContra() {
        return gContra;
    }

    public void setgContra(int gContra) {
        this.gContra = gContra;
    }

    public void agregarJugador(Jugador jugador) {
        this.jugadores.add(jugador);
    }

    @Override
    public String toString() {
        return carrera + "\t" + pJugados + "\t" + pGanados + "\t" + pPerdidos + "\t" + pEmpatados
                + "\t" + gFavor + "\t" + gContra + "\t";
    }

    public void incrementarGolesFavor() {
        this.gFavor++;
    }

    public void incrementarGolesContra() {
        this.gContra++;
    }

    public void incrementarPartidosJugados() {
        this.pJugados++;
    }

    public void incrementarPartidosGanados() {
        this.pGanados++;
    }

    public void incrementarPartidosEmpatados() {
        this.pEmpatados++;
    }

    public void incrementarPartidosPerdidos() {
        this.pPerdidos++;
    }

    public void setJugadores(ArrayList<Jugador> jugadores) {
        this.jugadores = jugadores;
    }

    public ArrayList<Jugador> getJugadores() {
        return jugadores;
    }
}
