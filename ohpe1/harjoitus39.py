#Halutun luvun kertotaulu 1-12.
luku = int(input("Ohjelma tulostaa halutun luvun kertotaulun 12 saakka.\nAnna kerrottava luku: "))
for i in range (1,13):
    print("{0} * {1} = {2} ".format(i,luku,luku*i))