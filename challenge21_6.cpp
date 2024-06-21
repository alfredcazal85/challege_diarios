#include <iostream>

using namespace std;

int main() {
    // Declaramos dos variables para almacenar los números ingresados por el usuario
    int num1, num2;

    // Solicitamos al usuario que ingrese el primer número
    cout << "Ingrese el primer número: ";
    cin >> num1;

    // Solicitamos al usuario que ingrese el segundo número
    cout << "Ingrese el segundo número: ";
    cin >> num2;

    // Calculamos la suma de los dos números
    int suma = num1 + num2;

    // Mostramos el resultado al usuario
    cout << "La suma de " << num1 << " y " << num2 << " es " << suma << endl;

    // Fin del programa
    return 0;
}
