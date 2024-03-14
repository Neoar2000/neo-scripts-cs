package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Biblioteca;

import java.time.LocalDate;
public class Prestamo {
	
	private Persona persona;
	private Libro libro;
	private LocalDate fechaPrestamo;
	private LocalDate fechaLimDevolucion;
	private LocalDate fechaRealDevolucion;
	private int estado;
	
	public Prestamo(Persona persona, Libro libro, 
			int d,int m,int a) {
		this.persona = persona;
		this.libro = libro;
		this.fechaPrestamo = LocalDate.of(a, m, d);
		// la fecha limite de devolucion es 15 dias despues del prestamo
		this.fechaLimDevolucion = fechaPrestamo.plusDays(15);
		this.fechaRealDevolucion = null;
		this.estado = 1;
		this.libro.prestar();
	}

	public Persona getPersona() {
		return persona;
	}

	public void setPersona(Persona persona) {
		this.persona = persona;
	}

	public Libro getLibro() {
		return libro;
	}

	public void setLibro(Libro libro) {
		this.libro = libro;
	}

	public LocalDate getFechaPrestamo() {
		return fechaPrestamo;
	}

	public void setFechaPrestamo(LocalDate fechaPrestamo) {
		this.fechaPrestamo = fechaPrestamo;
	}

	public LocalDate getFechaLimDevolucion() {
		return fechaLimDevolucion;
	}

	public void setFechaLimDevolucion(LocalDate fechaLimDevolucion) {
		this.fechaLimDevolucion = fechaLimDevolucion;
	}

	public LocalDate getFechaRealDevolucion() {
		return fechaRealDevolucion;
	}

	public void setFechaRealDevolucion(LocalDate fechaRealDevolucion) {
		this.fechaRealDevolucion = fechaRealDevolucion;
	}

	public int getEstado() {
		return estado;
	}

	public void setEstado(int estado) {
		this.estado = estado;
	}

	@Override
	public String toString() {
		return persona + "\t" + libro + "\t" + fechaPrestamo
				+ "\t" + fechaLimDevolucion + "\t" + fechaRealDevolucion
				+ "\t" + estado;
	}
	
	public void verificarPrestamo(int d,int m, int a ) {
		LocalDate actual = LocalDate.of(a, m, d);
		if(actual.isAfter(fechaLimDevolucion) && fechaRealDevolucion != null) {
			this.persona.setEnMora(true);
			this.libro.perdido();
			this.estado = 3;
		}
	}
	
	
	public void devolver(int d,int m, int a) {
		LocalDate actual = LocalDate.of(a, m, d);
		this.fechaRealDevolucion = actual;
		this.persona.setEnMora(false);
		this.libro.devolver();
		this.estado = 2;
	}
	
	
	
	
	
	
	
}
