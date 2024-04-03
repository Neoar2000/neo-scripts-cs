package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Cilindro_Herencia;

import javax.swing.*;

public class UsoCilindro {
    public static void main(String a[]) {
        JTextArea miArea = new JTextArea(10, 25);
        JScrollPane miScroll = new JScrollPane(miArea);

        Cilindro unCilindro = new Cilindro(1.0, 5.0);

        miArea.append("                      DATOS DEL CILINDRO\n");
        miArea.append("Radio: " + unCilindro.getRadio() + "\n");
        miArea.append("Altura: " + unCilindro.getAltura() + "\n");
        miArea.append("Área: " + unCilindro.obtenerArea() + "\n");
        miArea.append("Volumen: " + unCilindro.obtenerVolumen() + "\n");

        JOptionPane.showMessageDialog(null, miScroll);
        System.exit(0);
    }
}