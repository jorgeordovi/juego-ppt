from traceback import print_tb

nombre1 = input("Inserta tu nombre jugador 1 ")
nombre2 = input("Inserta tu nombre jugador 2 ")

jugador1 = input("Hola jugador 1. Elige piedra papel o tijera ")
jugador2 = input("Hola jugador 2. Elige piedra papel o tijera ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado el jugador 1")
else:
    print("Ha ganado el jugador 2")