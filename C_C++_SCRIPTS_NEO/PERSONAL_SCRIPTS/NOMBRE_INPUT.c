#include <stdio.h>

int main() {
    char nombre[20];
    char apellido[20];

    printf("Ingrese su nombre: ");
    scanf("%s", nombre);

    printf("\nIngrese su apellido: ");
    scanf("%s", apellido);

    printf("\nHola, %s %s!\n", nombre, apellido);

    return 0;
}