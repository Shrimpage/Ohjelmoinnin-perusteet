#Metodi palauttaa parametreistä suuremman tai yhtä suuren.

def Maksimi(eka,toka):
    if eka >= toka:
        return eka
    else:
        return toka

eka = int(input("Anna ensimmäinen luku: "))
toka = int(input("Anna toinen luku: "))

tulos = Maksimi(eka,toka)

print("Suurempi luvuista oli: " + str(tulos))
