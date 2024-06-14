# Solicitar al usuario que ingrese 5 números enteros
numeros = [] #cree una lista vacia para guardar los numeros
for i in range(5): #cree un bucle que se repetira en este caso 5 veces
    numero = int(input(f"Ingrese el número {i + 1}: ")) #Pido que el usuario ingrese 5 numeros i + 1 es para que diga numero 1, 2,3,4 y asi
    numeros.append(numero)

# Ordenar los números de manera ascendente y guara el resultado en numeros ordenados
numeros_ordenados = sorted(numeros)

# Mostrar los números ordenados
print("Los números ordenados de manera ascendente son:")
for numero in numeros_ordenados:
    print(numero)

