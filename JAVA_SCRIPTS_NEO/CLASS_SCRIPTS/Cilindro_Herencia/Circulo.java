package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Cilindro_Herencia;

public class Circulo {
    private double radio;

    public Circulo(double r) {
        radio = r;
    }

    public double getRadio() {
        return radio;
    }

    public double obtenerArea() {
        return Math.PI * Math.pow(radio, 2);
    }

    public double obtenerPerimetro() {
        return 2 * Math.PI * radio;
    }
}