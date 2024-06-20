import random
import string

def generar_contraseña(longitud): #establezco las condiciones de la longitud minima y maxima
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres.")

    # Caracteres a usar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Aseguramos que la contraseña tenga al menos una mayúscula, una minúscula, un número y un caracter especial
    contraseña = [
        random.choice(string.ascii_uppercase),  # Al menos una mayúscula
        random.choice(string.ascii_lowercase),  # Al menos una minúscula
        random.choice(string.digits),           # Al menos un número
        random.choice(string.punctuation)       # Al menos un caracter especial
    ]

    # Rellenamos el resto de la contraseña hasta alcanzar la longitud deseada
    contraseña += random.choices(caracteres, k=longitud - 4)

    # Mezclamos los caracteres para que no haya un patrón predecible
    random.shuffle(contraseña)

    # Convertimos la lista de caracteres en una cadena
    return ''.join(contraseña)

def main():
    # Generamos una longitud aleatoria entre 8 y 16
    longitud = random.randint(8, 16)
    contraseña = generar_contraseña(longitud)
    print(f"Tu contraseña segura es: {contraseña}")

if __name__ == "__main__":
    main()
