package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Biblioteca;

import java.time.LocalDate;

public class Prestamo {
    
    private Persona persona;
    private Libro libro;
    private LocalDate fechaPrestamo;
    private LocalDate fechaLimDevolucion;
    private LocalDate fechaRealDevolucion;
    private int estado;
    
    public Prestamo(Persona persona, Libro libro, int d, int m, int a) {
        this.persona = persona;
        this.libro = libro;
        this.fechaPrestamo = LocalDate.of(a, m, d);
        this.fechaLimDevolucion = fechaPrestamo.plusDays(15);
        this.fechaRealDevolucion = null;
        this.estado = 1; // Estado inicial: Activo
        this.libro.prestar(); // Marcar el libro como prestado
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
		String estadoStr = "";
		switch (estado) {
			case 1:
				estadoStr = "Activo";
				break;
			case 2:
				estadoStr = "Devuelto";
				break;
			case 3:
				estadoStr = "Vencido";
				break;
			default:
				estadoStr = "Estado desconocido";
				break;
		}
		return "Préstamo de: " + libro.getTitulo() + " a " + persona.getNombre() + ", Estado: " + estadoStr + "\n";
	}
    
    public void verificarPrestamo(int d, int m, int a) {
        LocalDate actual = LocalDate.of(a, m, d);
        if (actual.isAfter(fechaLimDevolucion) && fechaRealDevolucion == null) {
            // El préstamo está vencido
            this.estado = 3; // Estado: Vencido
            this.persona.setEnMora(true);
            this.libro.perdido(); // Marcar el libro como perdido
        }
    }
    
    public void devolver(int d, int m, int a) {
        if (fechaRealDevolucion == null) {
            LocalDate actual = LocalDate.of(a, m, d);
            this.fechaRealDevolucion = actual;
            this.persona.setEnMora(false);
            this.libro.devolver(); // Marcar el libro como devuelto
            this.estado = 2; // Estado: Devuelto
        } else {
            // El libro ya ha sido devuelto anteriormente
            System.out.println("El libro ya ha sido devuelto anteriormente.");
        }
    }
}