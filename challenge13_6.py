def contar_vocales(palabra):
    # Definir las vocales
    vocales = "aeiouAEIOU" 
    # Inicializar el contador de vocales
    contador = 0

    # Recorrer cada letra de la palabra
    for letra in palabra:
        # Si la letra es una vocal, incrementar el contador
        if letra in vocales:
            contador += 1

    return contador

# Palabra para contar las vocales
palabra = "terere"

# Llamar a la función y mostrar el resultado
numero_de_vocales = contar_vocales(palabra)
print(f"La palabra '{palabra}' tiene {numero_de_vocales} vocales.")
