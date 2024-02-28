package CLASS_SCRIPTS;

public class Rectangulo {
    private double base, altura;
    private String color;

    public Rectangulo(double base, double altura, String color) {
        this.base = base;
        this.altura = altura;
        this.color = color;
    }

    public double calcularArea() {
        return base * altura;
    }

    public void setBase(double base) {
        this.base = base;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public double getAltura() {
        return this.altura;
    }

    public double getBase() {
        return this.base;
    }

    public String getColor() {
        return this.color;
    }
    
    public String toString() {
        return "DATOS DEL RECTANGULO\n" + "Base: " + base + "\nAltura: " + altura + "\nColor: " + color + "\nArea: " + calcularArea();
    }
}
