import random
print("PIEDRA,PAPEL,...¡TIJERA!")
unoOpcion = random.choice(["PIEDRA","PAPEL","TIJERA","LAGARTO","SPOCK"])
dosOpcion = random.choice(["PIEDRA","PAPEL","TIJERA","LAGARTO","SPOCK"])
print("Jugador 1 ha sacado",unoOpcion)
print("Jugador 2 ha sacado",dosOpcion)

if unoOpcion == dosOpcion:
    print("Han empatado")
elif unoOpcion == "PIEDRA" and (dosOpcion == "SPOCK" or dosOpcion == "TIJERA"):
    print("Ha ganado Jugador 1")
elif unoOpcion == "PAPEL" and (dosOpcion == "PIEDRA" or dosOpcion == "LAGARTO"):
    print("Ha ganado Jugador 1")
elif unoOpcion == "TIJERA" and (dosOpcion == "SPOCK" or dosOpcion == "PAPEL"):
    print("Ha ganado Jugador 1")
elif unoOpcion == "LAGARTO" and (dosOpcion == "PIEDRA" or dosOpcion == "TIJERA"):
    print("Ha ganado Jugador 1")
elif unoOpcion == "SPOCK" and (dosOpcion == "PAPEL" or dosOpcion == "LAGARTO"):
    print("Ha ganado Jugador 1")
else:
    print("Ha ganado Jugador 2 ha sacado")