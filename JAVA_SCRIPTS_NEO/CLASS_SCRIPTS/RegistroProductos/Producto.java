package CLASS_SCRIPTS.RegistroProductos;
import java.io.*;
import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Producto {
	private int cod;
	private String nombre;
	private int cantidad;
	private double precio;
	private String descripcion;
	
	public Producto(int cod, String nombre, int cantidad, double precio, String descripcion) {
		
		this.cod = cod;
		this.nombre = nombre;
		this.cantidad = cantidad;
		this.precio = precio;
		this.descripcion = descripcion;
	}

	public int getCod() {
		return cod;
	}

	public void setCod(int cod) {
		this.cod = cod;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getCantidad() {
		return cantidad;
	}

	public void setCantidad(int cantidad) {
		this.cantidad = cantidad;
	}

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	@Override
	public String toString() {
		return cod + ";" + nombre + ";" + cantidad + ";" + precio
				+ ";" + descripcion;
	}
	
	
	public void registrarProductoTxt(String filename) {
		try {
			FileWriter escritor = new FileWriter(filename,true);
			escritor.write(this.toString()+"\n");
			escritor.close();
		}catch (IOException excp) {
			JOptionPane.showMessageDialog(null, excp.getMessage());
		}
	}
	
	
	public static ArrayList<Producto> leerProductosTxt(String filename) {
		ArrayList<Producto> productos =  new ArrayList<Producto>();
		String linea;
		try {
			BufferedReader lector =  new BufferedReader(new FileReader(filename));
			while((linea = lector.readLine())!= null) {
				
				String [] datos = linea.split(";");
				
				int cod = Integer.parseInt(datos[0]);
				String nombre = datos[1];
				String desc = datos[3];
				int cant = Integer.parseInt(datos[2]);
				double precio = Double.parseDouble(datos[3]);
				
				productos.add(new Producto(cod,nombre,cant,precio,desc));
				
			}
		}catch(IOException excp) {
			JOptionPane.showMessageDialog(null, excp.getMessage());
		}
		
		
		return productos;
	}
	
	
	public static void sobreEscribirProductosTxt(String filename,ArrayList<Producto> productos) {
		try {
			FileWriter escritor = new FileWriter(filename);
			for (Producto producto : productos) {
				escritor.write(producto.toString()+"\n");
			}
			escritor.close();
		}catch (IOException excp) {
			JOptionPane.showMessageDialog(null, excp.getMessage());
		}
	}
	
	
}
