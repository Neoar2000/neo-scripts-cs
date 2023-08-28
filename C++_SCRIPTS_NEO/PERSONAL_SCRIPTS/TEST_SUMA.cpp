#include <iostream>

int main () {
    int numero1;
    int numero2;

    std::cout << "Ingrese el primer numero: ";
    std::cin >> numero1;
    std::cout << "Ingrese el segundo numero: ";
    std::cin >> numero2;
    
    int suma = numero1 + numero2;

    std::cout << "La suma es: " << suma;
    return 0;
}