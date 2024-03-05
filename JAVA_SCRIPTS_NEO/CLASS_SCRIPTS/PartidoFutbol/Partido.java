import java.time.LocalDate;
import java.time.LocalTime;

public class Partido {
    private String equipoLocal, equipoVisitante, cancha;
    private int golesLocal, golesVisitante;
    private LocalDate fecha;
    private LocalTime horaInicio, horaFin;

    public void setPartido(String equipoLocal, String equipoVisitante, int golesLocal, int golesVisitante, int dia, int mes, int anio, String cancha, int horaInicio, int minInicio, int horaFin, int minFin) {
        this.equipoLocal = equipoLocal;
        this.equipoVisitante = equipoVisitante;
        this.golesLocal = golesLocal;
        this.golesVisitante = golesVisitante;
        this.fecha = LocalDate.of(anio, mes, dia);
        this.cancha = cancha;
        this.horaInicio = LocalTime.of(horaInicio, minInicio);
        this.horaFin = LocalTime.of(horaFin, minFin);
    }

    // Setters y Getters para equipoLocal
    public void setEquipoLocal(String equipoLocal) {
        this.equipoLocal = equipoLocal;
    }

    public String getEquipoLocal() {
        return equipoLocal;
    }

    // Setters y Getters para equipoVisitante
    public void setEquipoVisitante(String equipoVisitante) {
        this.equipoVisitante = equipoVisitante;
    }

    public String getEquipoVisitante() {
        return equipoVisitante;
    }

    // Setters y Getters para golesLocal
    public void setGolesLocal(int golesLocal) {
        this.golesLocal = golesLocal;
    }

    public int getGolesLocal() {
        return golesLocal;
    }

    // Setters y Getters para golesVisitante
    public void setGolesVisitante(int golesVisitante) {
        this.golesVisitante = golesVisitante;
    }

    public int getGolesVisitante() {
        return golesVisitante;
    }

    // Setters y Getters para fecha
    public void setFecha(int dia, int mes, int anio) {
        this.fecha = LocalDate.of(anio, mes, dia);
    }

    public LocalDate getFecha() {
        return fecha;
    }

    // Setters y Getters para cancha
    public void setCancha(String cancha) {
        this.cancha = cancha;
    }

    public String getCancha() {
        return cancha;
    }

    // Setters y Getters para horaInicio
    public void setHoraInicio(int hora, int minuto) {
        this.horaInicio = LocalTime.of(hora, minuto);
    }

    public LocalTime getHoraInicio() {
        return horaInicio;
    }

    // Setters y Getters para horaFin
    public void setHoraFin(int hora, int minuto) {
        this.horaFin = LocalTime.of(hora, minuto);
    }

    public LocalTime getHoraFin() {
        return horaFin;
    }

    public String toString() {
        return "Equipo Local: " + equipoLocal + "\nEquipo Visitante: " + equipoVisitante + "\nGoles Local: " + golesLocal + "\nGoles Visitante: " + golesVisitante + "\nFecha: " + fecha + "\nCancha: " + cancha + "\nHora de Inicio: " + horaInicio + "\nHora de Fin: " + horaFin;
    }
}