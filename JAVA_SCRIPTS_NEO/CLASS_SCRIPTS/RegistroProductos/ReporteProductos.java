package CLASS_SCRIPTS.RegistroProductos;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.BorderLayout;
import javax.swing.JLabel;
import java.awt.FlowLayout;
import java.awt.Color;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JCheckBox;
import javax.swing.JRadioButton;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;

import javax.swing.JList;
import javax.swing.AbstractListModel;

public class ReporteProductos extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;

	/**
	 * Launch the application.
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ReporteProductos frame = new ReporteProductos();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public ReporteProductos() {
		setTitle("Reporte");
		setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(new BorderLayout(0, 0));
		
		JPanel panTitulo = new JPanel();
		panTitulo.setBackground(new Color(64, 224, 208));
		contentPane.add(panTitulo, BorderLayout.NORTH);
		panTitulo.setLayout(new FlowLayout(FlowLayout.CENTER, 5, 5));
		
		JLabel lblTitulo = new JLabel("REPORTE DE PRODUCTOS");
		lblTitulo.setFont(new Font("Vensim Sans KR", Font.BOLD | Font.ITALIC, 13));
		panTitulo.add(lblTitulo);
		
		JPanel panReporte = new JPanel();
		contentPane.add(panReporte, BorderLayout.CENTER);
		panReporte.setLayout(new BorderLayout(0, 0));
		
		
		//Obtener los productos del archivo
		ArrayList<Producto> productos = Producto.leerProductosTxt(NombresArchivos.archivoProductosTxt);
		String values[] =  new String[productos.size()];
		int i = 0;
		for (Producto p : productos) {
			values[i] = p.getCod()+"\t"+p.getNombre()+"\t"+p.getCantidad()+"\t"+p.getPrecio()+"\t"+p.getDescripcion();
			i++;
		}
		
		
		JList listProductos = new JList();
		listProductos.setModel(new AbstractListModel() {
			
			public int getSize() {
				return values.length;
			}
			public Object getElementAt(int index) {
				return values[index];
			}
		});
		panReporte.add(listProductos, BorderLayout.CENTER);
		
		JPanel panBoton = new JPanel();
		FlowLayout fl_panBoton = (FlowLayout) panBoton.getLayout();
		fl_panBoton.setAlignment(FlowLayout.RIGHT);
		panReporte.add(panBoton, BorderLayout.SOUTH);
		
		JButton btnModificar = new JButton("Modificar Producto");
		panBoton.add(btnModificar);
		
		btnModificar.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				ModificarProducto mp = new ModificarProducto(productos.get(listProductos.getSelectedIndex()).getCod()); 
			}
		});
		
		setLocationRelativeTo(null); // Centra la ventana en la pantalla
		setVisible(true);
	}
}
