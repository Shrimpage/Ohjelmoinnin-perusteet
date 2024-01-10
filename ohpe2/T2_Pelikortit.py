# Tee ohjelma, jossa on tietorakenne korttipakan tietojen tallessa pitämiseksi. 
# Eli tietorakenteeseen voidaan tallentaa kortteja, joilla on tiedot: maa, arvo ja väri.
# Täytä tietorakenne toistorakenteen avulla siten, että rakenteesta löytyvät kaikki korttipakan kortit. 
# Arvo korttipakasta yksi kortti ja tulosta sen tiedot.

#lista jossa on tupleja (tuplessa kortin maa, arvo ja väri) eli listassa 52 alkiota

import random

print("Tämä ohjelma arvoo korttipakasta yhden kortin")

def main():
    kortit = ["Ässä","2","3","4","5","6","7","8","9","10","Jätkä","Kuningatar","Kuningas"]
    pakka = []
    vari = ""
    maa = ""
    for i1 in range(1,3):
        if i1 == 1:
            vari = "Punainen"
        elif i1 == 2:
            vari = "Musta"

        for i2 in range(1,3):
            if i1 == 1 and i2 ==1:
                maa = "Hertta"
            elif i1 == 1 and i2 ==2:
                maa = "Ruutu"
            elif i1 == 2 and i2 ==1:
                maa = "Pata"
            elif i1 == 2 and i2 ==2:
                maa = "Risti"

            for i3 in range(13):
                kortti = (kortit[i3])
                tuple = (vari,maa,kortti)
                pakka.append(tuple)

    while True:            
        inputti = input("Paina enter jatkaaksesi. (0 lopettaa ohjelman)")
        if inputti == "0":
            exit()
        else:
            rando = random.randint(0,53)
            print(pakka[rando])
            


if __name__ == '__main__':
    main()