#Onnen numerot
nimi = input("Tämä ohjelma laskee sinun onnen numerosi ja onnen kertoimen. Kerrotko koko nimesi? ")
pituus = input("Kerro pituutesi cm: ")
paino = input("Kerro painosi kg: ")
onumero = int(pituus) * int(paino) % 21
okerroin = float(onumero) / 4.3
print (str(nimi) + "\nOnnennumero: {0:.0f}\nOnnenkerroin: {1:.1f}".format(onumero,okerroin))