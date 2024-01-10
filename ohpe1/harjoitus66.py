#Metodi palauttaa arvonaan true, jos eka on suurempi,
#muuten se palauttaa arvon false.
print("ohjelma kertoo onko ensimmäinen luku suurempi.")
def EkaSuurempi(eka,toka):
    if eka > toka:
        return True
    else:
        return False

eka = int(input("Anna ensimmäinen luku: "))
toka = int(input("Anna toinen luku: "))

if EkaSuurempi(eka,toka):
    print("Arvo on True")
else:
    print("Arvo on False")