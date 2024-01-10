#Metodi palauttaa arvonaan true, jos parametrina saatu vuosi on karkausvuosi.

def Karkausvuosi(vuosi):
    if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
        return True
    else:
        return False
        
vuosi = int(input("Anna tarkasteltava vuosiluku: "))

if Karkausvuosi(vuosi):
    print("Tarkasteltu vuosi on karkausvuosi.")
else:
    print("Tarkasteltu vuosi ei ole karkausvuosi")