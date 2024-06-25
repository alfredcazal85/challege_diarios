#include <iostream>
#include <string>
#include <algorithm> // Para la función transform y reverse

using namespace std;

// Función para determinar si una palabra es un palíndromo
bool esPalindromo(string palabra) {
    // Convertir a minúsculas
    transform(palabra.begin(), palabra.end(), palabra.begin(), ::tolower);

    // Eliminar caracteres no alfabéticos
    palabra.erase(remove_if(palabra.begin(), palabra.end(), [](char c) { return !isalnum(c); }), palabra.end());

    // Comparar la palabra con su reverso
    string reverso = palabra;
    reverse(reverso.begin(), reverso.end());

    return palabra == reverso;
}

int main() {
    string palabra;

    cout << "Ingrese una palabra o frase: ";
    getline(cin, palabra);

    if (esPalindromo(palabra)) {
        cout << "Es un palíndromo." << endl;
    } else {
        cout << "No es un palíndromo." << endl;
    }

    return 0;
}
