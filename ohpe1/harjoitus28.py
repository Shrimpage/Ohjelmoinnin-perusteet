#Ohjelma kertoo annetusta luvusta tietoja
a = int(input("Anna kokonaisluku: "))
pari = a % 2

if a > 45 and a < 65:
    print("Lukusi on lukujen 45 ja 65 väliltä")
    if a > 0 and a < 150 and float(pari) == 0:
        print("Lukusi on parillinen ja nollaa suurempi, mutta pienempi kuin 150!")
elif a > 0 and a < 150 and float(pari) == 0:
    print("Lukusi on parillinen ja nollaa suurempi, mutta pienempi kuin 150!")