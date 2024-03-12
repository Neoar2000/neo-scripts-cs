import java.util.*;

//import java.time.LocalDate;
/*apuntes: se puede tener un array list de objetos, 
 el objeto se puede considerar un tipo de variable al declarar*/
public class Equipo {
	private String carrera;
	private ArrayList<Jugador> jugadores;
	private String capitan;
	//partidos
	private int pJugados;
	private int pGanados;
	private int pPerdidos;
	private int pEmpatados;
	//goles
	private int gFavor;
	private int gContra;
	public Equipo(String carrera, String capitan) {
		this.carrera = carrera;
		this.jugadores = new ArrayList<Jugador>();
		this.capitan = capitan;
		this.pJugados = 0;
		this.pGanados = 0;
		this.pPerdidos = 0;
		this.pEmpatados = 0;
		this.gFavor = 0;
		this.gContra = 0;
	}
	//geters y seters
	public String getCarrera() {
		return carrera;
	}
	public void setCarrera(String carrera) {
		this.carrera = carrera;
	}
	public void verJugadores() { //geter para ver jugadores
		for (Jugador jugador : jugadores) {
			System.out.println(jugador.toString());
		}
	}
	
	public String getCapitan() {
		return capitan;
	}
	public void setCapitan(String capitan) {
		this.capitan = capitan;
	}
	public int getpJugados() {
		return pJugados;
	}
	public void setpJugados(int pJugados) { //
		this.pJugados = pJugados;
	}
	public int getpGanados() {
		return pGanados;
	}
	public void setpGanados(int pGanados) {
		this.pGanados = pGanados;
	}
	public int getpPerdidos() {
		return pPerdidos;
	}
	public void setpPerdidos(int pPerdidos) {
		this.pPerdidos = pPerdidos;
	}
	public int getpEmpatados() {
		return pEmpatados;
	}
	public void setpEmpatados(int pEmpatados) {
		this.pEmpatados = pEmpatados;
	}
	public int getgFavor() {
		return gFavor;
	}
	public void setgFavor(int gFavor) {
		this.gFavor = gFavor;
	}
	public int getgContra() {
		return gContra;
	}
	public void setgContra(int gContra) {
		this.gContra = gContra;
	}
	
	//metodos:

	public void agregarJugador() {
		Scanner reader = new Scanner(System.in);
		System.out.println("		Registro de jugador		");
		System.out.println("ingrese el nombre del jugador");
		String nom = reader.nextLine();
		System.out.println("ingrese la posicion del jugador");
		String pos = reader.nextLine();
		System.out.println("ingrese el numero de camiseta del jugador");
		int jer = reader.nextInt();
		System.out.println("fecha de nacimiento");
		System.out.println("ingrese el dia");
		int d = reader.nextInt();
		System.out.println("ingrese el mes");
		int m = reader.nextInt();		
		System.out.println("ingrese el anho");
		int a = reader.nextInt();
		this.jugadores.add(new Jugador (nom, pos, jer, d, m, a));
	}
	@Override
	public String toString() {
		return carrera + "\t"+ pJugados+ "\t" + pGanados + "\t" + pPerdidos + "\t" + pEmpatados
				+ "\t" + gFavor + "\t" + gContra + "\t";
	}
	
	public void incrementarGolesFavor() {
		this.gFavor++;
	}
	
	public void incrementarGolesContra() {
		this.gContra++;
	}
	
	public void incrementarPartidosJugados() {
		this.pJugados++;
	}
	
	public void incrementarPartidosGanados() {
		this.pGanados++;
	}
	
	public void incrementarPartidosEmpatados() {
		this.pEmpatados++;
	}
	
	public void incrementarPartidosPerdidos() {
		this.pPerdidos++;
	}
	
	public void setJugadores(ArrayList<Jugador> jugadores) {
		this.jugadores = jugadores;
	}
	public ArrayList<Jugador> getJugadores() {
		return jugadores;
	}
}