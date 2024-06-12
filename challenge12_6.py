# El usuario ingresara los numeros que desea multiplicar, cada factor
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Aca se establece el titulo de la tabla, mostrando los numeros que eligio el usuario
print(f"Tabla de multiplicar de {num1} y {num2}:")

# Bucle para crear la tabla de multiplicar
for i in range(0, num2 + 1):
    resultado = num1 * i
    print(f"{num1} x {i} = {resultado}")
