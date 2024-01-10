#1.Tee metodi, jolla voi laskea taulukon solujen summan, metodi palauttaa summan.
luvut = [1,5,78,4,3,1,6,5,2,9,4,76,123,45,125,7,46,32,15,1]

def summa():
    return sum(luvut)
    
print("Lukujen summa on {0}".format(summa()))    

#2.Tee metodi, joka tulostaa kaikki parilliset luvut.

def parilliset():
    for luku in luvut:
        if luku % 2 == 0:
            print(luku)
            
parilliset()

#3.Tee metodi, joka etsii taulukon pienimmän luvun ja tulostaa sen.

def pienin():
    pienin = min(luvut)
    print("Pienin arvo = {0}".format(pienin))
    
pienin()    

#4.Tee metodi, joka tulostaa taulukon suurimman luvun indeksin.

def suurin():
    suurin = max(luvut)
    suurinindex = luvut.index(suurin)
    print("Suurimman luvun indexi on: " + str(suurinindex))

suurin()

#5.Tee metodi, jolla taulukosta voi etsiä parametrina annettua kokonaislukua. 
#Metodi palauttaa true tai false riippuen etsinnän tuloksesta.

def etsi(luku):
    if luku in luvut:
        return True
    else:
        return False
        
luku = int(input("Anna etsittävä luku: "))
print(etsi(luku))

#6.Tee metodi, joka laskee ja palauttaa tiedon, 
#kuinka monta kertaa parametrina annettu luku esiintyy taulukossa.

def montako(luvut,luku):
    return luvut.count(luku)
    
    
luku = int(input("Anna etsittävä luku: "))
print("{0} esiintyy {1} kertaa.".format(luku,montako(luvut,luku)))
   

#7.Tee metodi, joka tutkii ja palauttaa tiedon siitä, 
#missä solussa parametrina annettu luku esiintyy ensimmäisen kerran.

def para(luvut,paraluku):
    indexi = luvut.index(paraluku)
    print("Luvun {0} indeksi on {1}.".format(paraluku,indexi))

paraluku = int(input("Anna etsittävä luku: "))
para(luvut,paraluku)
