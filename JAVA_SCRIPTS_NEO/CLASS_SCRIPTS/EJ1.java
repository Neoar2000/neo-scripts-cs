package CLASS_SCRIPTS;

import java.text.SimpleDateFormat;
import java.util.*;

public class EJ1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la primera fecha (DD/MM/AAAA): ");
        String fechaStr1 = scanner.next();

        System.out.print("Ingrese la segunda fecha (DD/MM/AAAA): ");
        String fechaStr2 = scanner.next();

        Date fecha1 = parseFecha(fechaStr1);
        Date fecha2 = parseFecha(fechaStr2);

        long diferenciaMillis = Math.abs(fecha1.getTime() - fecha2.getTime());
        long diferenciaDias = diferenciaMillis / (1000 * 60 * 60 * 24);

        System.out.println("Hay " + diferenciaDias + " días entre las fechas.");

        scanner.close();
    }

    public static Date parseFecha(String fechaStr) {
        try {
            SimpleDateFormat formato = new SimpleDateFormat("dd/MM/yyyy");
            return formato.parse(fechaStr);
        } catch (java.text.ParseException e) {
            e.printStackTrace();
            return null;
        }
    }
}
