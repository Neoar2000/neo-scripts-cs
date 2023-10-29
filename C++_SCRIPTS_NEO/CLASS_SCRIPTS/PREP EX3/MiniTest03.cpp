#include <iostream>
#include <wchar.h>

using namespace std;

int generaSerie(int);
unsigned int factorial(unsigned int);

int main()
{
    setlocale(LC_ALL, "");
    int n;
    cout << "Cuantos elementos desea sumar?: ";
    cin >> n;
    cout << "La suma de los " << n << " elementos es: " << generaSerie(n);
    return 0;
}

int generaSerie(int n)
{
    if (n == 1)
        return 1;
    else
    {
        if (n % 3 == 0)
            return generaSerie(n-1) * factorial(n-1);
        else if (n % 3 == 1)
            return generaSerie(n-1) + factorial(n-1);
        else
            return generaSerie(n-1) - factorial(n-1);
    }
}

unsigned int factorial(unsigned int n)
{
    if (n == 0)
        n = 1;
    else
        n = n * factorial(n-1);
    return n;
}
