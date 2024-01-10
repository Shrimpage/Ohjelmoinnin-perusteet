#funktiot
def omaFunktio():
    print("Omassa funktiossa!")
    
omaFunktio()
omaFunktio()
omaFunktio()

def omaFunktio(nimi):
    print("Hei " + nimi)
    
omaFunktio("Matti")

def summa(luku1, luku2):
    return luku1 + luku2
    
vastaus = summa(2,8)

print("summa: " + str(vastaus))

def pienin(luku1, luku2):
    if luku1 < luku2:
        return luku1
    return luku2   

print(pienin(2,5)) 
print(pienin(8,3))   

def omaFunktio(nimi):
    print("Hei " + nimi + "!")

def summaa (luku1, luku2):
    tulos= luku1 + luku2
    return tulos

def pienin(luku1,luku2):
    if luku1 < luku2:
        return luku1 #poistutaan tästä
        
    return luku2    # poistutaan tästä jos luku2 on pienempi

omaFunktio("Masa")

print("summa: " + str(summa(12,8)))

print(pienin(2,5))
print(pienin(8,3))