#include <iostream>

int main () {
    int numero;

    std::cout << "Ingrese un numero: ";
    std::cin >> numero;
    
    if (numero % 2 == 0) {
        std::cout << "El numero " << numero << " es par";
    } else {
        std::cout << "El numero " << numero << " es impar";
    }
    
    return 0;
}