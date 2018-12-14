import random
print("JUEGO DEL QUINCE")
unoGloria = random.randrange(1,11)
dosGloria = random.randrange(1,11)
tresGloria = random.randrange(1,11)
unoHector = random.randrange(1,11)
dosHector = random.randrange(1,11)
tresHector = random.randrange(1,11)
print("Gloria ha sacado un ",unoGloria,", un ",dosGloria," y un ",tresGloria)
print("Héctor ha sacado un ",unoHector,", un ",dosHector," y un ",tresHector)
resultadoGloria = unoGloria + dosGloria + tresGloria
resultadoHector = unoHector + dosHector + tresHector
if resultadoGloria == resultadoHector:
    print("Han empatado")
elif resultadoGloria < 16 | resultadoGloria > resultadoHector:
        print("Ha ganado Gloria")
elif resultadoHector < 16 | resultadoHector > resultadoGloria:
        print("Ha ganado Héctor")
else:
    print("Han perdido los dos")
