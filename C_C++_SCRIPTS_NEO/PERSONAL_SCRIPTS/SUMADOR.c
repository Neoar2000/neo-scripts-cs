#include <stdio.h>

int main() {
    int num1, num2, suma;

    printf("Ingrese el primer numero: ");
    scanf("%d", &num1);
    
    printf("\nIngrese el segundo numero: ");
    scanf("%d", &num2);

    suma = num1 + num2;

    printf("\nLa suma de %d y %d es %d.\n", num1, num2, suma);

    return 0;
}