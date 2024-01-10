#tentti1
print("Tämä ohjelma laskee konttaukseen käytetyn kokonaisajan. ")
aika = float(input("Anna konttauksen aika sekunteina: "))
virheet = int(input("Anna tekniikkarikkeiden lukumäärä: "))
kokoaika = float((virheet*3)+aika)
print("Osallistuja käytti aikaa {0:.1f} sekuntia, rikkeitä oli {1}.\nKokonaisaika on {2:.1f} sekuntia".format(aika, virheet, kokoaika))