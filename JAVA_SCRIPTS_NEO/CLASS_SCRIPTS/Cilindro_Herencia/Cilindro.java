package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Cilindro_Herencia;

public class Cilindro extends Circulo {
    private double altura;

    public Cilindro(double r, double h) {
        super(r);
        altura = h;
    }

    public double getAltura() {
        return altura;
    }

    public double obtenerArea() {
        return obtenerPerimetro() * altura + 2 * super.obtenerArea();
    }

    public double obtenerVolumen() {
        return super.obtenerArea() * altura;
    }
}