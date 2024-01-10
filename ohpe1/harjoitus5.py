#Ohjelma joka laskee ja tulostaa tankatun bensiinin hinnan yhdellä lauseella

print("Tämä ohjelma laskee tankatun bensiinin hinnan")
litrahinta = input("Paljonko bensa maksaa? ")
tankattu = input("Montako litraa tankkasit? ")
summa = float(litrahinta) * float(tankattu)

muotoiltu_summa = "{:.2f}".format(summa)

print("Tankattiin " + str(tankattu) + " litraa, litrahinta on " + str(litrahinta) + ".\nYhteensä bensa maksaa "
+ str(muotoiltu_summa) + " E.")