summa = 0
erotus = 0
tulo = 0
osamaara = 0



def metodi(luku1, luku2, summa, erotus, tulo, osamaara):
    summa = luku1 + luku2
    erotus = luku1 - luku2
    tulo = luku1 * luku2
    osamaara = luku1 / luku2
    return summa, erotus, tulo, osamaara
    
luku1 = int(input("Anna 1. luku: "))
luku2 = int(input("Anna 2. luku: "))
print("Tässä niiden summa, erotus, tulo ja osamaara: ")
print(metodi(luku1, luku2, summa, erotus, tulo, osamaara))