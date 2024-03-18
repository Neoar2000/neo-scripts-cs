package JAVA_SCRIPTS_NEO.CLASS_SCRIPTS.Biblioteca;

import java.util.*;

public class Biblioteca {
    
    ArrayList<Persona> personas;
    ArrayList<Libro> libros;
    ArrayList<Prestamo> prestamos;
    
    public Biblioteca() {
        personas = new ArrayList<Persona>();
        libros = new ArrayList<Libro>();
        prestamos = new ArrayList<Prestamo>();
    }
    
    public void agregarLibro(int codigo, String titulo, String autor) {
		Libro nuevoLibro = new Libro(codigo, titulo, autor);
		libros.add(nuevoLibro);
		System.out.println("\nLibro agregado exitosamente.\n");
	}	
    
    public void agregarPersona(String ci, String nombre, String telefono, String correo) {
		Persona nuevaPersona = new Persona(ci, nombre, telefono, correo);
		personas.add(nuevaPersona);
		System.out.println("\nPersona agregada exitosamente.\n");
	}	
    
    public void agregarPrestamo(Prestamo prestamo) {
        prestamos.add(prestamo);
        System.out.println("\nPréstamo registrado exitosamente.\n");
    }
    
    public Libro buscarLibro(int cod) {
        for (Libro libro : libros) {
            if (libro.getCodigo() == cod) {
                return libro;
            }
        }
        return null;
    }
    
    public Persona buscarPersona(String ci) {
        for (Persona persona : personas) {
            if (persona.getCi().equals(ci)) {
                return persona;
            }
        }
        return null;
    }
    
    public Prestamo buscarPrestamo(int cod, String ci) {
		for (Prestamo prestamo : prestamos) {
			if (prestamo != null && prestamo.getLibro() != null && prestamo.getPersona() != null) {
				if (prestamo.getLibro().getCodigo() == cod && prestamo.getPersona().getCi().equals(ci)) {
					return prestamo;
				}
			}
		}
		return null;
	}	
    
    public void verificarPrestamos(int d, int m, int a) {
		boolean hayMorosos = false;
		System.out.println("Lista de morosos:\n");
		for (Prestamo p : prestamos) {
			p.verificarPrestamo(d, m, a);
			if (p.getEstado() == 3) { // Si el préstamo está vencido (estado 3)
				System.out.println(p); // Imprimir información relevante del préstamo
				hayMorosos = true;
			}
		}
		if (!hayMorosos) {
			System.out.println("No hay morosos en la fecha especificada.\n");
		}
	}	
}