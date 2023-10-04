#include <iostream>

using namespace std;

int promedio (int nota1, int nota2){
    return (nota1+nota2)/2;
}

int main() {
    int not1;
    int not2;
    
    cout << "Ingrese la nota del primer parcial: ";
    cin >> not1;
    
    cout << "Ingrese la nota del segundo parcial: ";
    cin >> not2;
    
    int resHab = promedio(not1, not2);
    
    cout << "Su nota de habilitacion es: " << resHab << endl;
    
    if (resHab >= 90){
        cout << "HABILITADO CON HONORES"<< endl;
    } else if (resHab >= 60 && resHab < 90){
        cout << "HABILITADO"<< endl;
    } else {
        cout << "REPROBADO"<< endl;
    }

    return 0;
}