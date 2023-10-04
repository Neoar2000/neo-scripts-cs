#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> numeros = {1, 2, 3, 4, 5};
    cout << "Los numeros del vector son: ";
    for (int i = 0; i < numeros.size(); i++) {
        cout << numeros[i] << " ";
    }
    
    numeros.push_back(6);
    
    cout << "\nAhora, los numeros del vector son: ";
    for (int i = 0; i < numeros.size(); i++) {
        cout << numeros[i] << " ";
    }
    
    cout << endl;

    return 0;
}
