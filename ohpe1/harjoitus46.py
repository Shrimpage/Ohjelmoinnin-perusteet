#ohjelma tulostaa kokeen arvosanan pistemäärän avulla.
keskiarvo = int(0)
i = int(0)
print("Tämä ohjelma selvittää kokeittesi arvosanat. Sekä niiden keskiarvon.")

while i > -1:
    pisteet = int(input("Anna pistemääräsi (0-60)(negatiivinen arvo pysäyttää kyselyn): "))
    if int(pisteet) <0:
        break
    elif int(pisteet) < 11:
        print("Arvosanasi on 0!")
        keskiarvo += pisteet
        i += 1 
    elif int(pisteet) <21:
        print("Arvosanasi on 1!")
        keskiarvo += pisteet
        i += 1 
    elif int(pisteet) <31:
        print("Arvosanasi on 2!")
        keskiarvo += pisteet
        i += 1 
    elif int(pisteet) <41:
        print("Arvosanasi on 3!")
        keskiarvo += pisteet
        i += 1 
    elif int(pisteet) <51:
        print("Arvosanasi on 4!")
        keskiarvo += pisteet
        i += 1 
    elif int(pisteet) <=60:
        print("Arvosanasi on 5!")
        keskiarvo += pisteet
        i += 1     
    else:
        print("Pisteet ylittävät maksimin! (0-60)(negatiivinen arvo pysäyttää kyselyn)")
if int(i) > 0:
    print("Sinä teit {0} koetta ja niiden pisteiden keskiarvo on {1:.2f} pistettä.".format(i,keskiarvo/i))
else:
    print("Et tehnyt yhtään koetta! :/")