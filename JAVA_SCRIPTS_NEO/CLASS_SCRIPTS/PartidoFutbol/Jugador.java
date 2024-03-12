import java.time.LocalDate; //local date

public class Jugador {
	private String nombre;
	private String posicion;
	private int jersey;
	private int golesAcumulados;
	private int tarjetasAmarillas;
	private boolean tarjetaRoja;
	private LocalDate fechaNacimiento;
	public Jugador(String nombre, String posicion, int jersey, int dia, int mes, int anho) {
		this.nombre = nombre;
		this.posicion = posicion;
		this.jersey = jersey;
		this.golesAcumulados = 0;
		this.tarjetasAmarillas = 0;
		this.tarjetaRoja = false;
		this.fechaNacimiento = LocalDate.of(anho, mes, dia);
	}
	//metodo to string
	@Override
	public String toString() {
		return nombre + "\t" + posicion + "\t" + jersey + "\t"
				+ golesAcumulados + "\t" + tarjetasAmarillas + "\t" + tarjetaRoja
				+ "\t" + fechaNacimiento;
	}
	//geters y seters
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getPosicion() {
		return posicion;
	}
	public void setPosicion(String posicion) {
		this.posicion = posicion;
	}
	public int getJersey() {
		return jersey;
	}
	public void setJersey(int jersey) {
		this.jersey = jersey;
	}
	public int getGolesAcumulados() {
		return golesAcumulados;
	}
	public void setGolesAcumulados(int golesAcumulados) {
		this.golesAcumulados = golesAcumulados;
	}
	public int getTarjetasAmarillas() {
		return tarjetasAmarillas;
	}
	public void setTarjetasAmarillas(int tarjetasAmarillas) {
		this.tarjetasAmarillas = tarjetasAmarillas;
	}
	public boolean isTarjetaRoja() {
		return tarjetaRoja;
	}
	public void setTarjetaRoja(boolean tarjetaRoja) {
		this.tarjetaRoja = tarjetaRoja;
	}
	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}
	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}
	
	
	//metodos
	public void IncrementarGoles() {
		this.golesAcumulados++;
	}
	public void IncrementarAmarillas() {
		this.tarjetasAmarillas++;
		if (this.tarjetasAmarillas>=2) {
			System.out.println("el jugador "+this.nombre+" se encuentra suspendido actualmente");
			this.tarjetaRoja = true;
			this.tarjetasAmarillas = 0;
		}
	}
	
	public boolean estaHabilitado() {
		if (getTarjetasAmarillas()<2) {
			System.out.println("el jugador "+this.nombre+" se encuentra habilitado");
			return true;
		}
		return false;
	}
	
	public void TarjetaRoja() {
		System.out.println("el jugador "+this.nombre+" se encuentra suspendido actualmente");
		this.tarjetaRoja = true;
		this.tarjetasAmarillas = 0;
	}

}