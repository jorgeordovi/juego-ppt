from traceback import print_tb


jugador1 = input("Hola jugador 1. Elige piedra papel o tijera ")
jugador2 = input("Hola jugador 2. Elige piedra papel o tijera ")

if jugador1 == jugador2:
    print("Ha sido un empate")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("Ha ganado el jugador 1")
else:
    print("Ha ganado el jugador 2")