package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Biblioteca;

public class Libro {
	private int codigo;
	private String titulo,autor;
	private int estado;
	
	public Libro(int codigo, String titulo, 
			String autor) {
		this.codigo = codigo;
		this.titulo = titulo;
		this.autor = autor;
		this.estado = 1;
	}

	public int getCodigo() {
		return codigo;
	}

	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}

	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public String getAutor() {
		return autor;
	}

	public void setAutor(String autor) {
		this.autor = autor;
	}

	public int getEstado() {
		return estado;
	}

	public void setEstado(int estado) {
		this.estado = estado;
	}
	
	public void prestar() {
		this.estado = 2;
	}
	
	public void devolver() {
		this.estado = 1;
	}
	
	public void perdido() {
		this.estado = 3;
	}

	@Override
	public String toString() {
		return codigo + "\t" + titulo + "\t" + autor + "\t" + estado;
	}
	
	
	
}

