#include <stdio.h>
#include <string.h>

int main() {
    char usr[20] = "ADMIN";
    char pwd[20] = "12345";
    char usr_input[20];
    char pwd_input[20];

    int autenticado = 0; // Variable para controlar la autenticación

    while (!autenticado) {
        printf("Ingrese su usuario: ");
        scanf("%s", usr_input);

        printf("\nIngrese su contrasenia: ");
        scanf("%s", pwd_input);

        // Verificar si las credenciales son correctas
        if (strcmp(usr_input, usr) == 0 && strcmp(pwd_input, pwd) == 0) {
            autenticado = 1; // Establecer autenticado a 1 para salir del bucle
        } else {
            printf("\nUsuario o contrasenia incorrectos. Intente nuevamente.\n\n");
        }
    }

    printf("\nInicio de sesion exitoso. Bienvenido, %s!\n", usr);

    return 0;
}
