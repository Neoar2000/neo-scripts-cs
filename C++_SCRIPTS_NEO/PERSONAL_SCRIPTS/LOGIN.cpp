#include <iostream>

using namespace std;

int main () {
    string usr;
    string pwd;

    cout << "Ingrese su usuario: ";
    cin >> usr;
    cout << "Ingrese su password: ";
    cin >> pwd;

    while (usr != "Neo" || pwd != "123") {
        cout << "Usuario y password incorrectos. Intente de nuevo." << endl;
        cout << "Ingrese su usuario: ";
        cin >> usr;
        cout << "Ingrese su password: ";
        cin >> pwd;
    }

    cout << "Bienvenido, " << usr << "!" << endl;

    return 0;
}