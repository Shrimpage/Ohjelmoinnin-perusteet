#ohjelma ilmoittaa veden olotilan sen lämpötilan perusteella.
aste = input("Kuinka lämmintä vesi on (Cº)? ")
if float(aste) < 0:
    print ("Vesi on jäässä!")
elif float(aste) >= 0 and float(aste) < 100:
    print ("Vesi on nestemäistä!")
else:
    print("Vesi on höyryä!")