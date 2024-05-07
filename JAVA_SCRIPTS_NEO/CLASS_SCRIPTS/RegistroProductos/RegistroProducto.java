import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;

import javax.swing.*;

public class RegistroProducto extends JFrame {
	JPanel panPrincipal;
	JPanel panTitulo;
	JPanel panFormulario;
	JPanel panBotones;
	JPanel panDatos;
	JPanel panDescripcion;
	JPanel pan11;
	JPanel pan12;
	JPanel pan21;
	JPanel pan22;
	
	JLabel lblTitulo;
	
	JButton btnAceptar;
	JButton btnLimpiar;
	JButton btnReporte;
	
	JLabel lblDescripcion;
	JTextArea txaDescripcion;
	
	JLabel lblCodigo;
	JLabel lblCantidad;
	JLabel lblPrecio;
	JLabel lblNombre;
	JTextField txtCodigo;
	JTextField txtCantidad;
	JTextField txtPrecio;
	JTextField txtNombre;
	
	public RegistroProducto() {
		setSize(500,300);
		setTitle("Registro de productos");
		setResizable(false);
		
		panPrincipal = new JPanel(new BorderLayout());
		this.getContentPane().add(panPrincipal);
		
		panTitulo = new JPanel(new FlowLayout(FlowLayout.CENTER));
		panFormulario =  new JPanel(new GridLayout(2,1));
		panBotones = new JPanel(new FlowLayout(FlowLayout.RIGHT));
		
		panPrincipal.add(panTitulo, BorderLayout.NORTH);
		panPrincipal.add(panFormulario, BorderLayout.CENTER);
		panPrincipal.add(panBotones, BorderLayout.SOUTH);
		
		lblTitulo = new JLabel("Registro de producto");
		panTitulo.add(lblTitulo);
		
		panDatos = new JPanel(new GridLayout(2,2));
		panDescripcion = new JPanel(new FlowLayout());
		panFormulario.add(panDatos);
		panFormulario.add(panDescripcion);
		
		pan11 =  new JPanel(new FlowLayout());
		pan12 =  new JPanel(new FlowLayout());
		pan21 =  new JPanel(new FlowLayout());
		pan22 =  new JPanel(new FlowLayout());
		panDatos.add(pan11);
		panDatos.add(pan12);
		panDatos.add(pan21);
		panDatos.add(pan22);
		
		lblCodigo =  new JLabel("Código: ");
		lblCantidad =  new JLabel("Cantidad: ");
		lblPrecio =  new JLabel("Precio: ");
		lblNombre =  new JLabel("Nombre: ");
		txtCodigo = new JTextField(15);
		txtCantidad = new JTextField(15);
		txtPrecio = new JTextField(15);
		txtNombre = new JTextField(15);
		
		pan11.add(lblCodigo);
		pan11.add(txtCodigo);
		pan12.add(lblCantidad);
		pan12.add(txtCantidad);
		pan21.add(lblNombre);
		pan21.add(txtNombre);
		pan22.add(lblPrecio);
		pan22.add(txtPrecio);
		
		lblDescripcion =  new JLabel("Descripción: ");
		txaDescripcion =  new JTextArea(5,30);
		panDescripcion.add(lblDescripcion);
		panDescripcion.add(txaDescripcion);
		
		
		btnAceptar = new JButton("ACEPTAR");
		btnLimpiar = new JButton("LIMPIAR");
		btnReporte = new JButton("VER PRODUCTOS");
		panBotones.add(btnAceptar);
		panBotones.add(btnLimpiar);
		panBotones.add(btnReporte);
		
		txtCodigo.addKeyListener(new KeyListener() {
			
			@Override
			public void keyTyped(KeyEvent e) {
				// TODO Auto-generated method stub
				
			}
			
			@Override
			public void keyReleased(KeyEvent e) {
				// TODO Auto-generated method stub
				int ultimo  = txtCodigo.getText().length()-1;
				String correcta = txtCodigo.getText();
				if(correcta.length()>0 &&(correcta.charAt(ultimo) < 48 || 
						txtCodigo.getText().charAt(ultimo) > 57)) {
					correcta = correcta.substring(0, ultimo);
				}
				txtCodigo.setText(correcta);
			}
			
			@Override
			public void keyPressed(KeyEvent e) {
				// TODO Auto-generated method stub
				int ultimo  = txtCodigo.getText().length()-1;
				String correcta = txtCodigo.getText();
				if(correcta.length()>0 &&(correcta.charAt(ultimo) < 48 || 
						txtCodigo.getText().charAt(ultimo) > 57)) {
					System.out.println("entra");
					correcta = correcta.substring(0, ultimo);
				}
				txtCodigo.setText(correcta);
			}
		});
		
		btnLimpiar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				txtCodigo.setText("");
				txtCantidad.setText("");
				txtPrecio.setText("");
				txtNombre.setText("");
				txaDescripcion.setText("");
			}
		});
		
		btnAceptar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				int cod,cant;
				double precio;
				String nombre,desc;
				
				cod = Integer.parseInt(txtCodigo.getText());
				nombre = txtNombre.getText();
				desc = txaDescripcion.getText();
				cant = Integer.parseInt(txtCantidad.getText());
				precio = Double.parseDouble(txtPrecio.getText());
				
				Producto nuevo  =  new Producto(cod,nombre,cant,precio,desc);
				nuevo.registrarProductoTxt(NombresArchivos.archivoProductosTxt);
				
				txtCodigo.setText("");
				txtCantidad.setText("");
				txtPrecio.setText("");
				txtNombre.setText("");
				txaDescripcion.setText("");
			}
		});
		
		btnReporte.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				ReporteProductos reporte = new ReporteProductos();
			}
		});
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLocationRelativeTo(null); // Centra la ventana en la pantalla
		setVisible(true);
	}
	
}
