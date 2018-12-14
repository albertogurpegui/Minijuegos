import random
print("JUEGO DE DADOS(2)")
unoCarmen = random.randrange(1,7)
dosCarmen = random.randrange(1,7)
unoDavid = random.randrange(1,7)
dosDavid = random.randrange(1,7)
print("Carmen ha sacado un ",unoCarmen, " y un ",dosCarmen)
print("David ha sacado un ",unoDavid," y un ",dosDavid)
resultadoCarmen = unoCarmen + dosCarmen
resultadoDavid = unoDavid + dosDavid
if resultadoCarmen == resultadoDavid:
    print("Han empatado")
elif resultadoCarmen > resultadoDavid:
    print("Ha ganado Carmen")
else:
    print("Ha ganado David")
