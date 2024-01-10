#Ohjelma laskee kuinka korkealle pesäpallo nousee lähtönopeuden perusteella
print("Tämä ohjelma laskee kuinka korkealle pesäpallo nousee syöttäjän kädestä lähtönopeuden perusteella")
lahto = float(input("Anna pesäpallon lähtönopeus m/s: "))
massa = 160
massag = float(massa)/1000
korkeus = (0.5*float(massag)*float(lahto)**2)/(float(massag)*9.81)
print("Pallo nousee korkeudelle {0:.2f} metriä.".format(korkeus))