import random #permite elegir cosas al azar

def obtener_eleccion_usuario(): #aqui se define la eleccion del usuario o jugador para presentar a la maquina
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ['piedra', 'papel', 'tijera']:
        eleccion = input("Elección inválida. Por favor elige piedra, papel o tijera: ").lower()
    return eleccion

def obtener_eleccion_maquina(): #aqui la maquina elige su opciòn de jugada
    elecciones = ['piedra', 'papel', 'tijera']
    return random.choice(elecciones)

def determinar_ganador(usuario, maquina): #aqui se establece las condiciones para el ganador 
    if usuario == maquina:
        return "Empate"
    elif (usuario == 'piedra' and maquina == 'tijera') or \
         (usuario == 'papel' and maquina == 'piedra') or \
         (usuario == 'tijera' and maquina == 'papel'):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar(): #se muestra las decisiones y el resultado o quien gano
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    usuario = obtener_eleccion_usuario()
    maquina = obtener_eleccion_maquina()
    print(f"Tú elegiste: {usuario}")
    print(f"La máquina eligió: {maquina}")
    resultado = determinar_ganador(usuario, maquina)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    jugar()
