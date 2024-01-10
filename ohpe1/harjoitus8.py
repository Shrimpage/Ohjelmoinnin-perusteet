#Ohjelma laskee mäkihyppääjän lentoajan
print("Tämä ohjelma laskee kuinka kauan mäkihyppääjä oli ilmassa.")
nopeus = input("Kuinka kova vauhti hyppääjällä oli km/h?    :")
aika = input("Kuinka pitkä hyppy oli metreinä?   :")
tulos = float(aika)/(float(nopeus)*(5/18))
print("Mäkihyppääjän lento kesti {0:.2f} sekuntia.".format(tulos))