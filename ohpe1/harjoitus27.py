#painoindeksiohjelma
print ("Tämä ohjelma laskee painoindeksisi.")
paino = float(input("Anna painosi (kg): "))
pituus = float(input("Anna pituutesi: "))
if pituus >10:
    pituusm = pituus/100
    indeksi = float(paino / (pituusm ** 2))
else:
    indeksi = float(paino / (pituus ** 2))
    
if indeksi < 18.5:
    print("Painoindeksisi on {0:.1f}.".format(indeksi))
    print("Olet alipainoinen!")
elif indeksi <= 25:
    print("Painoindeksisi on {0:.1f}.".format(indeksi))
    print("Olet normaalipainoinen!")
elif indeksi <= 30:
    print("Painoindeksisi on {0:.1f}.".format(indeksi))
    print("Olet lievästi ylipainoinen!")
elif indeksi <= 35:
    print("Painoindeksisi on {0:.1f}.".format(indeksi))
    print("Olet vakavasti ylipainoinen!")
else:
    print("Painoindeksisi on {0:.1f}.".format(indeksi))
    print("Olet sairaalloisen ylipainoinen!")