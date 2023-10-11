#include <iostream>
#include <cstdlib>
#include <iostream>
#include <locale>

using namespace std;

struct structFlota
{
    int nroBus;
    int tipoBus;
    int nroAsientos;
    int mayores;
    int adultos;
    int menores;
    int bebes;
    int ruta;
    double precio;
};

void llenarDatosBuses(structFlota[]);
void ventaPasajes(int, structFlota[]);
void reporteNroPersonasPorTipo(structFlota[]);
void reporteGananciasPorTipoPasajero(structFlota[]);
int asientosVendidos(int TipoBus);
int busesLlenos();
int busMayorGanacia();
int rutaMayorGanancia();

int main()
{
    int nroPasajes = 200;
    structFlota flotas[9];
    setlocale(LC_ALL, "");
    llenarDatosBuses(flotas);
    ventaPasajes(nroPasajes, flotas);
    reporteNroPersonasPorTipo(flotas);
    reporteGananciasPorTipoPasajero(flotas);
    return 0;
}

void llenarDatosBuses(structFlota flotas[])
{
    // Llenar el nro del bus
    flotas[0].nroBus = 1;
    flotas[1].nroBus = 2;
    flotas[2].nroBus = 3;
    flotas[3].nroBus = 4;
    flotas[4].nroBus = 5;
    flotas[5].nroBus = 6;
    flotas[6].nroBus = 7;
    flotas[7].nroBus = 8;
    flotas[8].nroBus = 9;

    // Llenar tipo del bus 1 = bus normal, 2 = bus cama, 3 = bus leito
    flotas[0].tipoBus = 1;
    flotas[1].tipoBus = 1;
    flotas[2].tipoBus = 1;
    flotas[3].tipoBus = 2;
    flotas[4].tipoBus = 2;
    flotas[5].tipoBus = 2;
    flotas[6].tipoBus = 3;
    flotas[7].tipoBus = 3;
    flotas[8].tipoBus = 3;

    // Llenar nro de asientos por tipo de bus
    flotas[0].nroAsientos = 40;
    flotas[1].nroAsientos = 40;
    flotas[2].nroAsientos = 40;
    flotas[3].nroAsientos = 30;
    flotas[4].nroAsientos = 30;
    flotas[5].nroAsientos = 30;
    flotas[6].nroAsientos = 20;
    flotas[7].nroAsientos = 20;
    flotas[8].nroAsientos = 20;

    flotas[0].ruta = 1;
    flotas[0].precio = 220;
    flotas[1].ruta = 2;
    flotas[1].precio = 130;
    flotas[2].ruta = 3;
    flotas[2].precio = 110;
    flotas[3].ruta = 1;
    flotas[3].precio = 300;
    flotas[4].ruta = 2;
    flotas[4].precio = 180;
    flotas[5].ruta = 3;
    flotas[5].precio = 150;
    flotas[6].ruta = 1;
    flotas[6].precio = 380;
    flotas[7].ruta = 2;
    flotas[7].precio = 240;
    flotas[8].ruta = 3;
    flotas[8].precio = 210;

    for (int i=0; i<9; i++)
    {
        flotas[i].mayores = 0;
        flotas[i].adultos = 0;
        flotas[i].menores = 0;
        flotas[i].bebes = 0;
    }
}

void ventaPasajes(int nroPasajes, structFlota flotas[])
{
    int nroFlota;
    int tipoPasajero;
    int totalPasajesFlota;
    for (int i=0; i<nroPasajes; i++)
    {
        do
        {
            nroFlota = 1 + rand() % (( 9 + 1) - 1);
            totalPasajesFlota = flotas[nroFlota-1].mayores + flotas[nroFlota-1].adultos + flotas[nroFlota-1].menores + flotas[nroFlota-1].bebes;
        }while (!(totalPasajesFlota < flotas[nroFlota-1].nroAsientos));

        tipoPasajero = 1 + rand() % (( 4 + 1) - 1);
        //cout << "Pasaje: " << i + 1 << endl;
        //cout << "Aleatorio nro flota: " << nroFlota << endl;
        //cout << "Aleatorio tipo pasajero: " << tipoPasajero << endl;
        switch (tipoPasajero)
        {
            case 1: // Mayores
                flotas[nroFlota-1].mayores++;
                break;
            case 2: // Adultos
                flotas[nroFlota-1].adultos++;
                break;
            case 3: // Menores
                flotas[nroFlota-1].menores++;
                break;
            case 4: // Bebes
                flotas[nroFlota-1].bebes++;
                break;
        }
    }
}

void reporteNroPersonasPorTipo(structFlota flotas[])
{
    int pasajerosMayores = 0;
    int pasajerosAdultos = 0;
    int pasajerosMenores = 0;
    int pasajerosBebes = 0;
    for (int i=0; i<9; i++)
    {
        pasajerosMayores += flotas[i].mayores;
        pasajerosAdultos += flotas[i].adultos;
        pasajerosMenores += flotas[i].menores;
        pasajerosBebes += flotas[i].bebes;
    }
    cout << "Nro pasajero mayores: " << pasajerosMayores << endl;
    cout << "Nro pasajero adultos: " << pasajerosAdultos << endl;
    cout << "Nro pasajero menores: " << pasajerosMenores << endl;
    cout << "Nro pasajero bebes: " << pasajerosBebes << endl;
}

void reporte(structFlota flotas[])
{
    for (int i=0; i<9; i++ )
    {
        cout << "FLORA NRO " << flotas[i].nroBus << endl;
        cout << "\tTipo: " << flotas[i].tipoBus << endl;
        cout << "\tNro Asientos: " << flotas[i].nroAsientos << endl;
        cout << "\tNro pasajes vendidos mayores: " << flotas[i].mayores << endl;
        cout << "\tNro pasajes vendidos adultos: " << flotas[i].adultos << endl;
        cout << "\tNro pasajes vendidos menores: " << flotas[i].menores << endl;
        cout << "\tNro pasajes vendidos bebes: " << flotas[i].bebes << endl;
        cout << "\tRuta: " << flotas[i].ruta << endl;
        cout << "\tPrecio: " << flotas[i].precio << "\n\n" << endl;
    }
}

void reporteGananciasPorTipoPasajero(structFlota flotas[])
{
    int gananciaMayores = 0;
    int gananciaAdultos = 0;
    int gananciaMenores = 0;
    int gananciaBebes = 0;
    for (int i=0; i<9; i++)
    {
        gananciaMayores += flotas[i].mayores * ( flotas[i].precio * 0.5);
        gananciaAdultos += flotas[i].adultos * flotas[i].precio;
        gananciaMenores += flotas[i].menores * ( flotas[i].precio * 0.6);
        gananciaBebes += flotas[i].bebes * ( flotas[i].precio * 0.1);
    }
    cout << "\n\nREPORTE DE GANANCIAS POR TIPO PASAJERO" << endl;
    cout << "======================================" << endl;;
    cout << "Ganancia de pasajero mayores: " << gananciaMayores  << endl;
    cout << "Ganancia de pasajero adultos: " << gananciaAdultos << endl;
    cout << "Ganancia de pasajero menores: " << gananciaMenores *0.6 << endl;
    cout << "Ganancia de pasajero bebes: " << gananciaBebes *0.1 << endl;
}

void reporteAsientosNoVendidos(structFlota flotas[])
{
    int gananciaMayores = 0;
    int gananciaAdultos = 0;
    int gananciaMenores = 0;
    int gananciaBebes = 0;
    for (int i=0; i<9; i++)
    {
        gananciaMayores += flotas[i].mayores * ( flotas[i].precio * 0.5);
        gananciaAdultos += flotas[i].adultos * flotas[i].precio;
        gananciaMenores += flotas[i].menores * ( flotas[i].precio * 0.6);
        gananciaBebes += flotas[i].bebes * ( flotas[i].precio * 0.1);
    }
    cout << "\n\nREPORTE DE GANANCIAS POR TIPO PASAJERO" << endl;
    cout << "======================================" << endl;;
    cout << "Ganancia de pasajero mayores: " << gananciaMayores  << endl;
    cout << "Ganancia de pasajero adultos: " << gananciaAdultos << endl;
    cout << "Ganancia de pasajero menores: " << gananciaMenores *0.6 << endl;
    cout << "Ganancia de pasajero bebes: " << gananciaBebes *0.1 << endl;
}