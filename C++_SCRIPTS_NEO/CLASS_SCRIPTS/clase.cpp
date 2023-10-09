#include <iostream>
#include <cstdlib>
#include <locale>

using namespace std;

struct Descendientes {
    int hijos = 0;
    int hijas = 0;
};

struct Empleado {
    string nombre;
    int ci;
    int departamento;
    int salario;
    Descendientes des;
};

void registrarDatos(Empleado&);
void mostrarDatos(Empleado);

int main () {
    Empleado empleado;
    registrarDatos(empleado);
    mostrarDatos(empleado);

    return 0;
}

void registrarDatos(Empleado &empleado) {
    srand(time(NULL));
    empleado.nombre;
    empleado.ci;
    empleado.departamento;
    empleado.salario;
    int n;
    int cantidadHijos;

    cout << "Ingrese su nombre: ";
    cin >> empleado.nombre;
    cout << "Ingrese su carnet de identidad: ";
    cin >> empleado.ci;
    cout << "Ingrese su departamento: ";
    cin >> empleado.departamento;
    cout << "Ingrese la cantidad de hijos: ";
    cin >> n;

    if (cantidadHijos <= n) {
        for (int i=1; i<n; i++) {
            empleado.des.hijos = 1 + rand() % ((n + 1) - 1);
            empleado.des.hijas = 1 + rand() % ((n + 1) - 1);
        }
    }

}

void mostrarDatos(Empleado empleado) {
    cout << "\n-- Datos del empleado --" << endl;
    cout << "Nombre: " << empleado.nombre << endl;
    cout << "Carnet de identidad: " << empleado.ci << endl;
    switch (empleado.departamento) {
        case 1:
            cout << "Departamento: Contabilidad" << endl;;
            empleado.salario = 100 + rand() % ((200 + 100) - 100);
            cout << "Salario: $" << empleado.salario << endl;;
            break;
        case 2:
            cout << "Departamento: Caja" << endl;;
            empleado.salario = 201 + rand() % ((300 + 201) - 201);
            cout << "Salario: $" << empleado.salario << endl;;
            break;
        case 3:
            cout << "Departamento: Biblioteca" << endl;;
            empleado.salario = 301 + rand() % ((400 + 301) - 301);
            cout << "Salario: $" << empleado.salario << endl;;
            break;
        case 4:
            cout << "Departamento: Admisiones" << endl;;
            empleado.salario = 401 + rand() % ((500 + 401) - 401);
            cout << "Salario: $" << empleado.salario << endl;;
            break;
        default:
            cout << "Departamento: NO DEFINIDO" << endl;;
            cout << "Salario: NO DEFINIDO" << endl;;
            break;
    }

    cout << "Hijos: " << empleado.des.hijos << endl;
    cout << "Hijas: " << empleado.des.hijas << endl;
}