# Joc: Endevinar nombre de 4 xifres
 
# Módul per escollir nombres aleatoriament
import random
 
# conjunt de símbols correctes pel codi
digits = ('0','1','2','3','4','5','6','7','8','9')
 
# "escollim" el codi
cant_digits = 4
codi = ''
for i in range(cant_digits):
    candidat = random.choice(digits)
    # anem escollint digits no repetits
    while candidat in codi:
        candidat = random.choice(digits)
    codi = codi + candidat
# començem la interacció amb l'usuari
print ("Ben vingut/a alumne d'SMX1 al Joc!")
print ("Hauràs d'endevinar un nombre de", cant_digits, 
      "xifres diferents")
print ("Si et dones, escriu: em dono ")
proposta = input("¿Quin codi esculls?: ")
 
# procesem les propostes i indiquem encerts i coincidencies
intents = 1
while proposta != codi and proposta != "em dono":
    intents = intents + 1
    encerts = 0
    coincidencies = 0
 
    # verifiquem la proposta i verifiquem el codi
    for i in range(cant_digits):
        if proposta[i] == codi[i]:
            encerts = encerts + 1
        elif proposta[i] in codi:
            coincidencies = coincidencies + 1
    print ("La teva proposta (", proposta, ") té", encerts, \
          "encerts i ", coincidencies, "coincidències.")
    # demanem següent proposta
    proposta = input("Escull un altre codi: ")
 
if proposta == "em dono":
    print ("El codi era", codi)
    print ("Sort per la propera!!")
    print ("Prem la tecla enter per finalitzar...")
    input ()
else:
    print ("Felicitas! Has encertat el codi en", \
    intents, "intents.")
    print ("Prem la tecla enter per finalitzar...")
    input ()
