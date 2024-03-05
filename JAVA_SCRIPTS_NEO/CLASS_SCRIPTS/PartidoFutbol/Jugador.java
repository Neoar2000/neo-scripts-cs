import java.time.*;

public class Jugador {
    private String nombre, posicion;
    private int nroCasaca, golesAcumulados, tarjetasAmarillas;
    private boolean tarjetaRoja;
    private LocalDate fechaNacimiento;

    public void setJugador(String nombre, String posicion, int nroCasaca, int dia, int mes, int anio) {
        this.nombre = nombre;
        this.posicion = posicion;
        this.nroCasaca = nroCasaca;
        this.golesAcumulados = 0;
        this.tarjetasAmarillas = 0;
        this.tarjetaRoja = false;
        this.fechaNacimiento = LocalDate.of(anio, mes, dia);
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public String getPosicion() {
        return posicion;
    }

    public int getNroCasaca() {
        return nroCasaca;
    }

    public int getGolesAcumulados() {
        return golesAcumulados;
    }

    public int getTarjetasAmarillas() {
        return tarjetasAmarillas;
    }

    public boolean tieneTarjetaRoja() {
        return tarjetaRoja;
    }

    public LocalDate getFechaNacimiento() {
        return fechaNacimiento;
    }

    public String toString() {
        return "Nombre: " + this.nombre + "\nPosicion: " + this.posicion + "\nNro de casaca: " + this.nroCasaca + "\nGoles acumulados: " + this.golesAcumulados + "\nTarjetas amarillas: " + this.tarjetasAmarillas + "\nTarjeta roja: " + this.tarjetaRoja + "\nFecha de nacimiento: " + this.fechaNacimiento.getDayOfMonth()+"/"+this.fechaNacimiento.getMonthValue()+"/"+this.fechaNacimiento.getYear();
    }
}
