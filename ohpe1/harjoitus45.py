#kokonaiskalori ja keskiarvo laskuri
summa = 0
keskiarvo = 0

print("Tämä ohjelma laskee tietyn ajan kokonaiskalorimäärän ja päiväkeskiarvon.")
i = 0
while i > -1:
    kalorit = int(input("Anna päivän kalorit. (0 lopettaa kyselyn)"))
    summa += kalorit
    if kalorit == 0:
        break
    i += 1
keskiarvo = summa/i
print("{0} päivän kokonaiskalorimäärä oli {1} ja keskiarvo päivälle oli {2}.".format(i,summa,keskiarvo))