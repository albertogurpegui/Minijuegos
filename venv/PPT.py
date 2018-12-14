import random
print("PIEDRA,PAPEL,...¡TIJERA!")
inesOpcion = random.choice(["PIEDRA","PAPEL","TIJERA"])
juanOpcion = random.choice(["PIEDRA","PAPEL","TIJERA"])
print("Inés ha sacado",inesOpcion)
print("Juan ha sacado",juanOpcion)

if inesOpcion == "PIEDRA" and juanOpcion == "TIJERA":
    print("Ha ganado Inés")
elif inesOpcion == "PAPEL" and juanOpcion == "PIEDRA":
    print("Ha ganado Inés")
elif inesOpcion == "TIJERA" and juanOpcion == "PAPEL":
    print("Ha ganado Inés")
elif inesOpcion == juanOpcion:
    print("Han empatado")
else:
    print("Ha ganado Juan")