#include <stdio.h>

int main() {
    int num1, num2, suma;

    printf("Ingrese el primer numero: ");
    scanf("%d", &num1);
    
    printf("\nIngrese el segundo numero: ");
    scanf("%d", &num2);

    suma = num1 + num2;

    printf("\nEl resultado de la suma es: %d\n", suma);

    return 0;
}