def somma(numeri = [1,2,3,4]):
    totale = 0

    for n in numeri:
        if n % 2 == 0:
            totale += n
    return totale

def Inversione():
    stringa_inv = ("".join(reversed(stringa)))
    return stringa_inv

def paroleLunghe(parole):
    parole_lunghe = []
    for p in parole:
        if len(p) > 5:
            parole_lunghe.append(p)
    return parole_lunghe

def numGrande(numeri):
    numero_grande = max(numeri)
    return numero_grande

def parolaLunga(parole):
    parola_lunga = ''
    for p in parole:
        if len(p) > len(parola_lunga):
            parola_lunga = p
    return parola_lunga

def conversioneIntero(numero):
    return int(numero)

def conversioneStringa(numero):
    return str(numero)

def numeriInteri(lista):
    for n in range(len(lista)):
        lista[n] = int(lista[n])
    return lista

def conversioneStringa(lista):
    for n in range(len(lista)):
        lista[n] = str(lista[n])
    return lista

def separazioneCifre(numero):
    lista_cifre = []
    for c in str(numero):
        lista_cifre.append(int(c))
    return lista_cifre