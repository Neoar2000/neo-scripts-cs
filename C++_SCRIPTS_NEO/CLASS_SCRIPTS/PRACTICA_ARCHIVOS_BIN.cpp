#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

struct structEstudiante
{
    char ci[10];
    char nombres[30];
    char apellidos[30];
};

struct structNotas
{
    char ci[10];
    char materia[30];
    int nota;
};

void ingresarEstudiante()
{
    structEstudiante estudiante;

    system("cls");
    cout << "\tINGRESO DE DATOS ESTUDIANTE" << endl;
    cout << "==============================================" << endl;
    cout << "CI: ";
    cin >> estudiante.ci;

    ifstream archivoLecturaEstudiantes("Estudiantes.bin", ios::binary);
    if (archivoLecturaEstudiantes)
    {
        structEstudiante estudianteExistente;
        while (archivoLecturaEstudiantes.read(reinterpret_cast<char*>(&estudianteExistente), sizeof(estudianteExistente)))
        {
            if (strcmp(estudiante.ci, estudianteExistente.ci) == 0)
            {
                system("cls");
                cout << "Este CI ya esta registrado. Ingrese un CI diferente.\n" << endl;
                system("pause");
                return;
            }
        }
        archivoLecturaEstudiantes.close();
    }

    cout << "Nombres: ";
    cin.ignore();
    cin.getline(estudiante.nombres, sizeof(estudiante.nombres));
    cout << "Apellidos: ";
    cin.getline(estudiante.apellidos, sizeof(estudiante.apellidos));

    ofstream archivoEscrituraEstudiantes("Estudiantes.bin", ios::binary | ios::app);
    archivoEscrituraEstudiantes.write(reinterpret_cast<char*>(&estudiante), sizeof(estudiante));
    archivoEscrituraEstudiantes.close();

    system("cls");
    cout << "Estudiante ingresado correctamente.\n" << endl;
    system("pause");
}

void ingresarNotas()
{
    structNotas notas;

    system("cls");
    cout << "\t\tINGRESO DE NOTAS" << endl;
    cout << "==============================================" << endl;
    cout << "CI del estudiante: ";
    cin >> notas.ci;

    ifstream archivoLecturaNotas("Notas.bin", ios::binary);
    if (archivoLecturaNotas)
    {
        structNotas notaExistente;
        while (archivoLecturaNotas.read(reinterpret_cast<char*>(&notaExistente), sizeof(notaExistente)))
        {
            if (strcmp(notas.ci, notaExistente.ci) == 0)
            {
                system("cls");
                cout << "Este estudiante ya tiene una nota registrada. Ingrese un CI diferente.\n" << endl;
                system("pause");
                return;
            }
        }
        archivoLecturaNotas.close();
    }

    ifstream archivoEstudiantes("Estudiantes.bin", ios::binary);
    if (!archivoEstudiantes)
    {
        cerr << "Error al abrir el archivo de estudiantes." << endl;
        return;
    }

    bool estudianteEncontrado = false;
    structEstudiante estudiante;
    while (archivoEstudiantes.read(reinterpret_cast<char*>(&estudiante), sizeof(estudiante)))
    {
        if (strcmp(notas.ci, estudiante.ci) == 0)
        {
            estudianteEncontrado = true;
            break;
        }
    }

    archivoEstudiantes.close();

    if (!estudianteEncontrado)
    {
        system("cls");
        cout << "Estudiante no encontrado. Ingrese el estudiante primero.\n" << endl;
        system("pause");
        return;
    }

    cout << "\nNombres: " << estudiante.nombres << endl;
    cout << "Apellidos: " << estudiante.apellidos << endl;
    cout << "\nMateria: ";
    cin.ignore();
    cin.getline(notas.materia, sizeof(notas.materia));
    cout << "Nota: ";
    cin >> notas.nota;

    ofstream archivoNotas("Notas.bin", ios::binary | ios::app);
    archivoNotas.write(reinterpret_cast<char*>(&notas), sizeof(notas));
    archivoNotas.close();

    system("cls");
    cout << "Notas ingresadas correctamente.\n" << endl;
    system("pause");
}

void reporteEstudiantesNotas()
{
    system("cls");
    cout << "\tREPORTE DE ESTUDIANTES Y NOTAS" << endl;
    cout << "==============================================" << endl;

    ifstream archivoNotas("Notas.bin", ios::binary);
    if (!archivoNotas)
    {
        cerr << "Error al abrir el archivo de notas." << endl;
        return;
    }

    structNotas notas;
    while (archivoNotas.read(reinterpret_cast<char*>(&notas), sizeof(notas)))
    {
        ifstream archivoEstudiantes("Estudiantes.bin", ios::binary);
        if (!archivoEstudiantes)
        {
            cerr << "Error al abrir el archivo de estudiantes." << endl;
            return;
        }

        structEstudiante estudiante;
        bool estudianteEncontrado = false;
        while (archivoEstudiantes.read(reinterpret_cast<char*>(&estudiante), sizeof(estudiante)))
        {
            if (strcmp(notas.ci, estudiante.ci) == 0)
            {
                estudianteEncontrado = true;
                break;
            }
        }

        archivoEstudiantes.close();

        if (estudianteEncontrado)
        {
            cout << "Nombres: " << estudiante.nombres << endl;
            cout << "Apellidos: " << estudiante.apellidos << endl;
            cout << "CI: " << estudiante.ci << endl;
            cout << "Materia: " << notas.materia << endl; 
            cout << "Nota: " << notas.nota << endl;
            cout << "==============================================" << endl;
        }
    }

    archivoNotas.close();

    cout << "\n";
    system("pause");
}

int main()
{
    int opcion;

    do
    {
        system("cls");
        cout << "\tSISTEMA DE REGISTRO ACADEMICO" << endl;
        cout << "==============================================" << endl;
        cout << "1. Ingreso de datos estudiante." << endl;
        cout << "2. Ingreso de materias y notas." << endl;
        cout << "3. Reporte de estudiantes y notas ingresadas." << endl;
        cout << "4. Salir." << endl;
        cout << "Ingrese la opcion: ";
        cin >> opcion;

        switch (opcion)
        {
        case 1:
            ingresarEstudiante();
            break;
        case 2:
            ingresarNotas();
            break;
        case 3:
            reporteEstudiantesNotas();
            break;
        case 4:
            system("cls");
            cout << "Saliendo del sistema. Hasta luego!" << endl;
            break;
        default:
            system("cls");
            cout << "Opcion no valida. Por favor, ingrese una opcion valida.\n" << endl;
            system("pause");
            break;
        }
    } while (opcion != 4);

    return 0;
}