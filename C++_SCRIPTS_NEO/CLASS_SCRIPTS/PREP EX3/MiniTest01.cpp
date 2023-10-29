#include <iostream>
#include <wchar.h>

using namespace std;

int generaSerie(int);
bool esPrimo(int, int);

int main()
{
    int n;
    setlocale(LC_ALL, "");
    cout << "Cuantos números desea generar: ";
    cin >> n;
    for(int i=1; i<=n; i++)
        cout << generaSerie(i) << "\t";
    return 0;
}

int generaSerie(int x)
{
    if (x == 1)
        return 1;
    else if (x == 2)
        return 2;
    else
    {
        if (esPrimo(generaSerie(x-1),2))
            return generaSerie(x-1) + generaSerie(x-2);
        else
            return generaSerie(x-1) + generaSerie(x-2) + generaSerie(x-3);
    }
}

bool esPrimo(int numero, int divisor)
{
    if(divisor < numero)
    {
        if(numero%divisor != 0)
            return esPrimo(numero, divisor+1);
        else
            return false;
    }
    return true;
}
