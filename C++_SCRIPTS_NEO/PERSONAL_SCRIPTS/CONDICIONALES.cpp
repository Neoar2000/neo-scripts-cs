#include <iostream>

int main () {
    int num1;
    int num2;

    std::cout << "Ingrese el primer numero: ";
    std::cin >> num1;
    std::cout << "Ingrese el segundo numero: ";
    std::cin >> num2;

    if (num1 == num2) {
        std::cout << "Son iguales";
    } else {
        std::cout << "No son iguales";
    }
}