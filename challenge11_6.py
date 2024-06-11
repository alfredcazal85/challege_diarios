def invertir_caracteres(cadena_de_caracteres):
    if len(cadena_de_caracteres) == 0:
        return ""
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1]) #la primera parte toma la ultima letra de la palabra, se llama a la funcion y se le da la palabra sin la ultima letra, hasta que se acabe

# Pedir al usuario que ingrese una palabra
palabra = input("Ingresa una palabra para invertir: ")

# Llamar a la función con la palabra ingresada por el usuario
resultado = invertir_caracteres(palabra)

# Imprimir el resultado
print(resultado)