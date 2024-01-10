#Ohjelma joka laskee nettopalkan
print("Tämä ohjelma laskee nettopalkkasi.")
brut = input("Paljonko palkkasi on ennen veroja? ")
vero = input("Kuinka suuri on veroprosenttisi? ")
netto = float(brut)-float(brut)*float(vero)/100
print("Käteen jäävä nettopalkka on {0:.2f} euroa.".format(netto))