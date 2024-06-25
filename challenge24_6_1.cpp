#include <iostream>
using namespace std;

int main() {
    const int TAMANO = 10;
    int numeros[TAMANO];

    // Solicitar al usuario que ingrese los números
    cout << "Ingrese 10 números enteros:" << endl;
    for (int i = 0; i < TAMANO; i++) {
        cout << "Número " << (i + 1) << ": ";
        cin >> numeros[i];
    }

    // Algoritmo de ordenación de burbuja
    for (int i = 0; i < TAMANO - 1; i++) {
        for (int j = 0; j < TAMANO - i - 1; j++) {
            if (numeros[j] > numeros[j + 1]) {
                // Intercambiar numeros[j] y numeros[j + 1]
                int temp = numeros[j];
                numeros[j] = numeros[j + 1];
                numeros[j + 1] = temp;
            }
        }
    }

    // Mostrar los números ordenados
    cout << "Números ordenados de menor a mayor:" << endl;
    for (int i = 0; i < TAMANO; i++) {
        cout << numeros[i] << " ";
    }
    cout << endl;

    return 0;
}
