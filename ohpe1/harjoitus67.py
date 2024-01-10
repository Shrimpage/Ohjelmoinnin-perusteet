#Ohjelmoi metodi Valuutta, joka laskee paljonko asiakas saa toista valuuttaa valuutanvaihdossa. Metodi saa tiedon vaihdettavasta summasta ja käytettävästä kurssista.. Metodi palauttaa saadun summan.

def Valuutta(summa,kurssi):
    return summa*kurssi
    
summa = float(input("Anna muunnettavan valuutan määrä: "))
kurssi = float(input("Anna muunnoskurssi: "))

print("Näin paljon saat toista valuuttaa {0:.02f}".format(Valuutta(summa,kurssi)))