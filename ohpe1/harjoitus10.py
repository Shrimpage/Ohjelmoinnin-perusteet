#Ohjelma laskee kunka kauan matka kestää
print("Tämä ohjelma laksee kuinka kauan matka kestää.")
matka = float(input("Kuinka pitkä matka on päämäärääsi? "))
nopeus = float(input("Ilmoita matkasi keskinopeus: "))
tunnit = float(matka)//float(nopeus)
minuutit = (float(matka)/float(nopeus)-float(tunnit))*60
print("Matka aika on {0:.0f} tuntia ja {1:.0f} minuuttia.".format(tunnit,minuutit))

#Myös int() voidaan käyttää muuttamaan lukuja kokonaisluvuiksi.
#esim: aika = matka / keskinopeus
#tunnit = int(aika) 
#minuutit = int((aika-tunnit) *60)