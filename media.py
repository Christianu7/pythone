ultimoNumero = input("inserire il primo numero: ")
contatore = 0
sommaParziale = 0

if not ultimoNumero.isdigit() :
    print("Fornire almeno un numero")
    exit()

while ultimoNumero.isdigit():
    contatore += 1
    sommaParziale += float(ultimoNumero)
    ultimoNumero = input("Inserire il prossimo numero: ")
print("la media dei numeri passati è:", sommaParziale/contatore)