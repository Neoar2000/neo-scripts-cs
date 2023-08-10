#include <iostream>
#include <cmath>

int main () {
    int numero;
    int exponente;
    std::cout << "Ingrese un numero: ";
    std::cin >> numero;
    std::cout << "Ingrese la exponente: ";
    std::cin >> exponente;
    int potencia = pow(numero, exponente);

    std::cout << numero << " elevado a " << exponente << " es: " << potencia;
}