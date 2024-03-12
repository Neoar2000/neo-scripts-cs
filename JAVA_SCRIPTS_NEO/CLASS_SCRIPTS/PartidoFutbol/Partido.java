import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;

public class Partido {
	private Equipo equipoLocal;
	private Equipo equipoVisitante;
	private int gLocal;
	private int gVisitante;
	private LocalDate fecha;
	private LocalTime horaInicio;
	private LocalTime horaFin;
	
	private String cancha; //posiblemente lo saquemos

	public Partido(Equipo equipoLocal, Equipo equipoVisitante,
			int d, int m, int a, String cancha) {
		this.equipoLocal = equipoLocal;
		this.equipoVisitante = equipoVisitante;
		this.gLocal = 0;
		this.gVisitante = 0;
		this.fecha = LocalDate.of(a, m, d);
		this.horaInicio = LocalTime.now();
		this.horaFin = null;
		this.cancha = cancha;
	}

	public Equipo getEquipoLocal() {
		return equipoLocal;
	}

	public void setEquipoLocal(Equipo equipoLocal) {
		this.equipoLocal = equipoLocal;
	}

	public Equipo getEquipoVisitante() {
		return equipoVisitante;
	}

	public void setEquipoVisitante(Equipo equipoVisitante) {
		this.equipoVisitante = equipoVisitante;
	}

	public int getgLocal() {
		return gLocal;
	}

	public void setgLocal(int gLocal) {
		this.gLocal = gLocal;
	}

	public int getgVisitante() {
		return gVisitante;
	}

	public void setgContra(int gContra) {
		this.gVisitante = gContra;
	}

	public LocalDate getFecha() {
		return fecha;
	}

	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}

	public LocalTime getHoraInicio() {
		return horaInicio;
	}

	public void setHoraInicio(LocalTime horaInicio) {
		this.horaInicio = horaInicio;
	}

	public LocalTime getHoraFin() {
		return horaFin;
	}

	public void setHoraFin(LocalTime horaFin) {
		this.horaFin = horaFin;
	}

	public String getCancha() {
		return cancha;
	}

	public void setCancha(String cancha) {
		this.cancha = cancha;
	}

	@Override
	public String toString() {
		return cancha +"\t" + equipoLocal.getCarrera() + "\t" + equipoVisitante.getCarrera() + 
				"\t" + fecha + "\t" + horaInicio + "\t" + horaFin ;
	}
	
	public void golLocal(int casaca) {
		this.gLocal++;
		this.equipoLocal.incrementarGolesFavor();
		for (Jugador j:equipoLocal.getJugadores()) {
			if(j.getJersey()==casaca) {
				j.IncrementarGoles();
			}
		}
		this.equipoVisitante.incrementarGolesContra();
	}
	
	public void golVisitante(int casaca) {
		this.gVisitante++;
		this.equipoVisitante.incrementarGolesFavor();
		for (Jugador j:equipoVisitante.getJugadores()) {
			if(j.getJersey()==casaca) {
				j.IncrementarGoles();
			}
		}
		this.equipoLocal.incrementarGolesContra();
	}
	
	public void amarillaLocal(int casaca) {
		for (Jugador j:equipoLocal.getJugadores()) {
			if(j.getJersey()==casaca) {
				j.IncrementarAmarillas();
			}
		}
	}
	
	public void amarillaVisitante(int casaca) {
		for (Jugador j:equipoVisitante.getJugadores()) {
			if(j.getJersey()==casaca) {
				j.IncrementarAmarillas();
			}
		}
	}
	
	public void rojaLocal(int casaca) {
		for (Jugador j:equipoLocal.getJugadores()) {
			if(j.getJersey()==casaca) {
				j.TarjetaRoja();
			}
		}
	}
	
	public void rojaVisitante(int casaca) {
		for (Jugador j:equipoVisitante.getJugadores()) {
			if(j.getJersey()==casaca) {
				j.TarjetaRoja();
			}
		}
	}
	
	public void terminarPartido(){
		this.equipoLocal.incrementarPartidosJugados();
		this.equipoVisitante.incrementarPartidosJugados();
		if(this.gLocal > this.gVisitante) {
			this.equipoLocal.incrementarPartidosGanados();
			this.equipoVisitante.incrementarPartidosPerdidos();
		}else if(this.gLocal==this.gVisitante) {
			this.equipoLocal.incrementarPartidosEmpatados();
			this.equipoVisitante.incrementarPartidosEmpatados();
		}else {
			this.equipoLocal.incrementarPartidosPerdidos();
			this.equipoVisitante.incrementarPartidosGanados();
		}
		this.horaFin = LocalTime.now();
	}
}