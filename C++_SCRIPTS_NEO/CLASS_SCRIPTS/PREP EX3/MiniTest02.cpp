#include <iostream>
#include <wchar.h>
#include <cstdlib>

using namespace std;

int sumaValores(int[], int);
void llenarVector(int[], int);
void mostrarVector(int[], int);

int main()
{
    setlocale(LC_ALL, "");
    srand(time(NULL));
    int vector1[100];
    int n;
    cout << "Cuantos elementos tiene el vector?: ";
    cin >> n;
    llenarVector(vector1, n);
    mostrarVector(vector1, n);
    cout << "\nLa suma de sus valores es: " << sumaValores(vector1,n-1);
    return 0;
}

void llenarVector(int vector1[], int n)
{
    for (int i=0; i<n; i++)
        vector1[i] = 1 + rand() % (( 100 + 1) - 1);
}

void mostrarVector(int vector1[], int n)
{
    for (int i=0; i<n; i++)
        cout << vector1[i] << "\t";
}


int sumaValores(int vector1[], int n)
{
    if (n == 0)
    {
        if (vector1[0] % 2 == 0)
            return vector1[0];
        else
            return vector1[0] * (-1);
    }
    else
    {
        if (vector1[n] % 2 == 0)
            return sumaValores(vector1, n - 1) + vector1[n];
        else
            return sumaValores(vector1, n - 1) - vector1[n];
    }
}
