#include <iostream>
#include <fstream>

using namespace std;

const int MAX_ESTUDIANTES = 100;

struct Estudiante {
    char nombres[30];
    char apellidos[30];
    char materia[100];  // Aumentar el tamaño para permitir espacios en la materia
    int nota;
};

void ingresarDatos() {
    ofstream archivo("Personas.txt", ios::app);

    if (!archivo.is_open()) {
        cerr << "El archivo NO se puede abrir o es inexistente." << endl;
        return;
    }

    Estudiante estudiante;

    string nombre;
    string apellidos;
    string materia;
    int nota;

    char respuesta;

    do {
        cout << "Ingrese el nombre: ";
        cin >> nombre;

        cout << "Ingrese el(los) apellido(s): ";
        cin >> apellidos;

        cout << "Ingrese la materia: ";
        cin.ignore();  // Limpiar el buffer antes de getline
        getline(cin, materia);

        cout << "Ingrese la nota: ";
        cin >> nota;

        archivo << nombre << ';' << apellidos << ';' << materia << ';' << nota << '\n';

        cout << "Desea ingresar otro estudiante? (s/n): ";
        cin >> respuesta;

        cin.ignore();

    } while (respuesta == 's' || respuesta == 'S');

    archivo.close();
}

void leerArchivo(Estudiante estudiantes[], int& numEstudiantes) {
    ifstream archivo("Personas.txt");

    if (!archivo.is_open()) {
        cerr << "El archivo NO se puede abrir o es inexistente." << endl;
        return;
    }

    numEstudiantes = 0;

    while (archivo.getline(estudiantes[numEstudiantes].nombres, 30, ';') &&
           archivo.getline(estudiantes[numEstudiantes].apellidos, 30, ';') &&
           archivo.getline(estudiantes[numEstudiantes].materia, 100, ';') &&
           (archivo >> estudiantes[numEstudiantes].nota)) {

        archivo.ignore();

        numEstudiantes++;

        if (numEstudiantes >= MAX_ESTUDIANTES) {
            cerr << "Se ha alcanzado el límite máximo de estudiantes." << endl;
            break;
        }
    }

    archivo.close();
}

int main() {
    Estudiante estudiantes[MAX_ESTUDIANTES];
    int numEstudiantes = 0;

    ingresarDatos();
    leerArchivo(estudiantes, numEstudiantes);

    cout << "\nLISTA DE ESTUDIANTES REGISTRADOS" << endl;
    cout << "==================================" << endl;

    for (int i = 0; i < numEstudiantes; i++) {
        cout << "Nombre: " << estudiantes[i].nombres << " " << estudiantes[i].apellidos << endl;
        cout << "Materia: " << estudiantes[i].materia << endl;
        cout << "Nota: " << estudiantes[i].nota << endl;
        cout << "==========================" << endl;
    }

    return 0;
}