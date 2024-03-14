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
	
	public void agregarLibro() {
		
	}
	
	public void agregarPersona() {
		
	}
	
	public void agregarPrestamo() {
		
	}
	
	public Libro buscarLibro(int cod) {
		return null;
	}
	
	public Persona buscarPersona(String ci) {
		return null;
	}
	
	public Persona buscarPrestamo(int cod, String ci) {
		return null;
	}
	
	public void verificarPrestamos(int d, int m, int a) {
		for(Prestamo p:prestamos) {
			p.verificarPrestamo(d,m,a);
		}
	}
	
}
