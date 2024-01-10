#a) Pinta-ala neliöstä
luku1 =input("Tämä ohjelma laskee neliön pinta-alan. Syötä neliön sivun pituus: ")
neliönala = int(luku1) ** 2

print("Neliön pinta-ala on: " + str(neliönala))

#b) Ympyrän Pinta-ala
import math
luku2 =input("Seuraavaksi ohjelma laskee ympyrän pinta-alan. Syötä ympyrän säde: ")
ympyränala = math.pi * float(luku2) * float(luku2)

print("Ympyrän pinta-ala on: {0:.2f} " .format(ympyränala))

#c) Suorakulmion pinta-ala kokonaislukuina
luku3 = int(input("Seuraavaksi ohjelma laskee suorakulmion pinta-alan. Syötä ensimmäisen sivun pituus: "))

luku4 = int(input("Syötä toisen sivun pituus: "))
suorakulmionala = int(luku3) * int(luku4)

print("Suorakulmion pinta-ala on: " + str(suorakulmionala))

#d) Kolmion pinta-ala
luku5 = input("Seuraavaksi ohjelma laskee kolmion pinta-alan. Syötä kolmion kannan mitta: ")

luku6 = input("Syötä kolmion korkeus: ")
kolmionala = int(luku5) * int(luku6) / 2

print("Kolmion pinta-ala on: " + str(kolmionala))

#e) Kaikkien pinta-ala
print("Seuraavaksi ohjelma tulostaa kaikkien pinta-alojen summan.")
summa = float(kolmionala) + float(suorakulmionala) + float(ympyränala) + float(neliönala)

muotoiltu_summa = "{:.2f}".format(summa)
float_summa = float(muotoiltu_summa)

print("Pinta-alat yhteensä: " + str(float_summa))