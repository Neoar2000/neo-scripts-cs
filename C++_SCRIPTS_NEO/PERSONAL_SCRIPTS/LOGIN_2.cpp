#include <iostream>

using namespace std;

int main() {
    string usr;
    string pwd;
    
    cout << "Ingrese su usuario: ";
        cin >> usr;
        cout << "Ingrese su password: ";
        cin >> pwd;
    
    while (usr != "admin" or pwd != "123"){
        cout << "User and password incorrect." << endl;
        cout << "Ingrese su usuario: ";
        cin >> usr;
        cout << "Ingrese su password: ";
        cin >> pwd;
    }
    
    cout << "Bienvenido al sistema!" << endl;
    
    return 0;
}