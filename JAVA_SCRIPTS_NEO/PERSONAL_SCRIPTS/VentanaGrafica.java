package PERSONAL_SCRIPTS;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class VentanaGrafica extends JFrame {
    
    public VentanaGrafica() {
        setTitle("Ventana Grafica");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        
        JButton botonHola = new JButton("Hola");
        JButton botonAdios = new JButton("Adios");
        
        botonHola.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "¡Hola!");
            }
        });
        
        botonAdios.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int confirmacion = JOptionPane.showConfirmDialog(null, "¿Seguro que quieres salir?", "Confirmación", JOptionPane.YES_NO_OPTION);
                if (confirmacion == JOptionPane.YES_OPTION) {
                    System.exit(0);
                }
            }
        });
        
        panel.add(botonHola);
        panel.add(botonAdios);
        
        add(panel);
        
        // Centrar la ventana en la pantalla
        setLocationRelativeTo(null);
        
        setVisible(true);
    }
    
    public static void main(String[] args) {
        new VentanaGrafica();
    }
}