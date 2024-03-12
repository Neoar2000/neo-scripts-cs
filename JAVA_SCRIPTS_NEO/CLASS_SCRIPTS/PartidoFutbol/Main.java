public class Main {

	public static void main(String[] args) {
		Equipo sistemas = new Equipo("Ing. de Sistemas", "Orlando Rivera");
		Equipo mecatronica = new Equipo("Ing. Mecatronica","Fabio Diaz");
		
		sistemas.getJugadores().add(new Jugador("Willy Tenorio","Arquero",1,5,1,1978));
		sistemas.getJugadores().add(new Jugador("Wilder Orellana","Medio",7,28,12,1988));
		sistemas.getJugadores().add(new Jugador("Daniel Calderon","Delant",10,6,6,1965));
		
		mecatronica.getJugadores().add(new Jugador("Gabriel Rojas","Arquero",1,5,1,1992));
		mecatronica.getJugadores().add(new Jugador("Guillermo Man","Medio",7,28,12,1993));
		mecatronica.getJugadores().add(new Jugador("Diego Calderon","Delant",10,6,6,1990));
		
		System.out.println(sistemas);
		sistemas.verJugadores();
		System.out.println(mecatronica);
		mecatronica.verJugadores();
		
		Partido p1 = new Partido(sistemas, mecatronica, 13, 3, 2024, "Arquitectura");
		System.out.println(p1);
		
		p1.golLocal(7);
		p1.golLocal(10);
		p1.golLocal(10);
		p1.amarillaVisitante(10);
		p1.golVisitante(1);
		p1.rojaLocal(7);
		p1.golVisitante(10);
		
		p1.terminarPartido();
		System.out.println(p1);
		System.out.println("--------------------------------------------");
		System.out.println(sistemas);
		System.out.println(mecatronica);
		System.out.println("--------------------------------------------");
		sistemas.verJugadores();
		mecatronica.verJugadores();
	}

}