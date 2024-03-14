package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Biblioteca;

public class Persona {
	private String ci,nombre,telefono,correo;
	private boolean enMora;
	
	public Persona(String ci, String nombre, String telefono, 
			String correo) {
		this.ci = ci;
		this.nombre = nombre;
		this.telefono = telefono;
		this.correo = correo;
		this.enMora = false;
	}

	@Override
	public String toString() {
		return  ci + "\t" + nombre + "\t" + telefono + "\t" + correo
				+ "\t" + enMora;
	}

	public String getCi() {
		return ci;
	}

	public void setCi(String ci) {
		this.ci = ci;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public String getCorreo() {
		return correo;
	}

	public void setCorreo(String correo) {
		this.correo = correo;
	}

	public boolean isEnMora() {
		return enMora;
	}

	public void setEnMora(boolean enMora) {
		this.enMora = enMora;
	}
	
	
}
