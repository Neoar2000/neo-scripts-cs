#include <iostream>
#include <chrono>
#include <thread>

using namespace std;

int main() {
    int opcion;

    while (true) {
        cout << "Selecciona una opcion:" << endl;
        cout << "1. Opcion 1" << endl;
        cout << "2. Opcion 2" << endl;
        cout << "3. Opcion 3" << endl;
        cout << "4. Salir del programa" << endl;
        cout << "\nIngresa el numero de opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "\nHas seleccionado la Opcion 1.\n" << endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                break;
            case 2:
                cout << "\nHas seleccionado la Opcion 2.\n" << endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                break;
            case 3:
                cout << "\nHas seleccionado la Opcion 3.\n" << endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                break;
            case 4:
                cout << "\nSaliendo del programa..." << endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                return 0;
            default:
                cout << "\nOpcion no valida. Por favor, selecciona una opcion valida.\n" << endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                break;
        }
    }

    return 0;
}
