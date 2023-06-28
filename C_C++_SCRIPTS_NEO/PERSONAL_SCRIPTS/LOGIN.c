#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_INTENTOS 3

int main() {
    char usr[20] = "ADMIN";
    char pwd[20] = "12345";
    char usr_input[20];
    char pwd_input[20];

    int autenticado = 0; // Variable para controlar la autenticación
    int intentos = 0; // Variable para controlar el número de intentos

    system("clear");

    while (!autenticado && intentos < MAX_INTENTOS) {
        printf("Ingrese su usuario: ");
        fgets(usr_input, sizeof(usr_input), stdin);
        usr_input[strcspn(usr_input, "\n")] = '\0'; // Eliminar el carácter de nueva línea

        printf("\nIngrese su contraseña: ");
        fgets(pwd_input, sizeof(pwd_input), stdin);
        pwd_input[strcspn(pwd_input, "\n")] = '\0'; // Eliminar el carácter de nueva línea

        // Verificar si las credenciales son correctas
        if (strcmp(usr_input, usr) == 0 && strcmp(pwd_input, pwd) == 0) {
            autenticado = 1; // Establecer autenticado a 1 para salir del bucle
        } else {
            system("clear");
            printf("Usuario o contrasenia incorrectos. Intente nuevamente.\n\n");
            intentos++;
        }
    }

    if (autenticado){
        system("clear");
        printf("Inicio de sesion exitoso. Bienvenido, %s!\n", usr);
    } else {
        system("clear");
        printf("Ha excedido el numero maximo de intentos.\n");
    }

    return 0;
}
