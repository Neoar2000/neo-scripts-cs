#include <iostream>
#include <vector>

using namespace std;

int main () {
    vector<int> vec;
    int num;

    while (true){
        cout << "Ingrese un numero entero (0 para salir): ";
        cin >> num;

        if (num == 0) {
            break;
        }

        vec.push_back(num);
    }

    cout << "Los elementos ingresados al vector son: ";
    
    for (int i = 0; i < vec.size(); ++i) {
        cout << vec[i] << ' ';
    }

    return 0;
}