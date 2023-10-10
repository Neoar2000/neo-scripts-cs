#include <iostream>
#include <cstdlib>
#include <iostream>
#include <locale>

using namespace std;

// Definir la estructura de la flota
struct structtFlota
{
    int nroBus;
    int tipoBus;
    int nroAsientos;
    int ruta;
    double precio;
};

// Prototipos de funciones
void llenarDatosBuses(structtFlota[]);
void reporteBuses(structtFlota[], int);

int main()
{
    structtFlota flotas[4];
    setlocale(LC_ALL, "");
    llenarDatosBuses(flotas);
    reporteBuses(flotas,4);
    return 0;
}

void llenarDatosBuses(structtFlota flotas[])
{
    // Flota 1
    flotas[0].nroBus = 1;
    flotas[0].tipoBus = 1;
    flotas[0].nroAsientos = 40;
    flotas[0].ruta = 1;
    flotas[0].precio = 220;
    // Flota 2
    flotas[1].nroBus = 2;
    flotas[1].tipoBus = 1;
    flotas[1].nroAsientos = 40;
    flotas[1].ruta = 2;
    flotas[1].precio = 130;
    // Flota 3
    flotas[2].nroBus = 3;
    flotas[2].tipoBus = 2;
    flotas[2].nroAsientos = 30;
    flotas[2].ruta = 1;
    flotas[2].precio = 300;
    // Flota 4
    flotas[3].nroBus = 4;
    flotas[3].tipoBus = 2;
    flotas[3].nroAsientos = 30;
    flotas[3].ruta = 2;
    flotas[3].precio = 180;
}

void reporteBuses(structtFlota flotas[], int nroFlotas)
{
    int tipoPasajero; // 1: bebe, 2:niño, 3:adulto, 4:3ra edad
    srand(time(NULL));
    for (int i=0; i<nroFlotas; i++)
    {
        cout << "Nro de bus: " << flotas[i].nroBus + 1 << endl;
        switch (flotas[i].tipoBus)
        {
            case 1:
                cout << "Tipo bus: NORMAL" << endl;;
                break;
            case 2:
                cout << "Tipo bus: CAMA" << endl;;
                break;
            case 3:
                cout << "Tipo bus: LEITO" << endl;;
                break;
            default:
                cout << "Tipo bus: NO DEFINIDO" << flotas[i].tipoBus << endl;;
                break;
        }
        cout << "Nro asientos: " << flotas[i].nroAsientos << endl;
        switch (flotas[i].ruta)
        {
            case 1:
                cout << "Ruta: LPZ - SCZ - LPZ" << endl;;
                break;
            case 2:
                cout << "Ruta: LPZ -CBB - LPZ" << endl;;
                break;
            default:
                cout << "Ruta: NO DEFINIDO" << flotas[i].tipoBus << endl;;
                break;
        }
        cout << "Precio: " << flotas[i].precio << endl;
        /* initialize random seed: */
        tipoPasajero = 1 + rand() % (( 4 + 1) - 1);
        switch (tipoPasajero)
        {
            case 1: // 1: infante
                cout << "El pasajero es: INFANTE " << endl;
                break;
            case 2: // 2:niño
                cout << "El pasajero es: NIÑO" <<  endl;
                break;
            case 3: // 3:adulto
                cout << "El pasajero es: ADULTO" <<  endl;
                break;
            case 4: // 4:3ra edad
                cout << "El pasajero es: 3ra EDAD" <<  endl;
                break;
            default:
                cout << "Ruta: NO DEFINIDO" << flotas[i].tipoBus << endl;;
                break;
        }
        cout << endl << endl;
    }
}