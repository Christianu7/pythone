SCAGLIONE1=27000
SCAGLIONE2=40000
SCAGLIONE3=53000
TASSA_SC1=0.23
TASSA_SC2=0.35
TASSA_SC3=0.43
reddito = float(input ("Che reddito hai?")) #Inserimento reddito
print("Il tuo reddito 0 ",reddito,"euro")
if reddito <= SCAGLIONE1 :
    aliquota = reddito *TASSA_SC1
    print("Le tue tasse sono",aliquota,"euro")
else :  
     if reddito <= SCAGLIONE2 :
        aliquota = SCAGLIONE1 * TASSA_SC1 + (reddito - SCAGLIONE1)*TASSA_SC2
        print("Le tue tasse sono",aliquota,"euro")
     else:
        aliquota = SCAGLIONE1 * TASSA_SC1 + (SCAGLIONE2-SCAGLIONE1)*TASSA_SC2 + (reddito - SCAGLIONE2)*TASSA_SC3
        print("Le tue tasse sono",aliquota,"euro")
