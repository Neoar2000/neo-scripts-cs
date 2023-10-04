#include <iostream>
#include <string>

using namespace std;

struct Estudiante {
    string nombre;
    int edad;
    string semestre;

    void mostrarDatos () {
        cout << "Datos del estudiante\n" << endl;
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << endl;
        cout << "Semestre: " << semestre << endl;
    }
};

int main () {
    Estudiante p = {"Neo", 23, "2do"};
    Estudiante s = {"Roman", 19, "2do"}; 
    p.mostrarDatos();
    return 0;
}