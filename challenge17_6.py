def crear_diccionario(claves, valores):
    """
    Crea un diccionario a partir de dos listas: una de claves y otra de valores.

    Args:
    claves (list): Lista de claves.
    valores (list): Lista de valores.

    Returns:
    dict: Diccionario resultante de combinar las claves y los valores.
    """
    # Verifica que las listas tengan la misma longitud, si no hay igual cantidad de elementos 
    
    if len(claves) != len(valores):
        raise ValueError("Las listas de claves y valores deben tener la misma longitud")

    # Crea el diccionario usando la función zip, que une las listas en pares y crean el diccionario
    diccionario = dict(zip(claves, valores))

    return diccionario

# Ejemplo de uso
claves = ["Nombre", "Apellido", "Edad", "Ciudad", "Barrio", "Estado_Civil"]
valores = ["Alfredo", "Cazal", 38, "Lambare", "Santo Domingo", "Casado"]

diccionario = crear_diccionario(claves, valores)
print(diccionario)
