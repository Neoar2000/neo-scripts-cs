package CLASS_SCRIPTS;

public class Fecha {
    public int dia, mes, anio;

    public Fecha(int dia, int mes, int anio) {
        this.dia = dia;
        this.mes = mes;
        this.anio = anio;
    }

    public String toString() {
        return "La fecha ingresada es: " + dia + "/" + mes + "/" + anio;
    }
}
