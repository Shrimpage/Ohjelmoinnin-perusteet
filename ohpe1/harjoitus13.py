#Ohjelma laskee kuinka paljon kauemmin köröttelijän matka kestää
print("Tämä ohjelma laskee kuinka paljon kauemmin köröttelijän matka Helsingistä Seinäjoelle kestää kuin kaaharin.")
kaaha = input("Anna kaaharin keskinopeus: ")
koro = input("Anna köröttelijän keskinopeus: ")
matka = 359
kaahat = float(matka)//float(kaaha)
kaaham = float(matka)/float(kaaha)%1*60
korot = float(matka)//float(koro)
korom = float(matka)/float(koro)%1*60
erot = float(matka)/float(koro)-float(matka)/float(kaaha)
erom = float(erot)%1*60
print ("Välillä Seinäjoki - Helsinki köröttelijälle meni aikaa {0:.0f} tuntia {1:.1f} minuuttia enemmän kuin kaaharilla.".format(erot,erom))
print ("Kaaharilta meni aikaa {0:.0f} tuntia {1:.1f} minuuttia.".format(kaahat,kaaham))
print ("Köröttelijältä meni aikaa {0:.0f} tuntia {1:.1f} minuuttia.".format(korot,korom))


#Välillä Seinäjoki - Helsinki köröttelijällä 
#meni aikaa 1 tunti 5 minuuttia enemmän kuin kaaharilla.
#Kaaharilta meni aikaa 3 tuntia 25 minuuttia.
#Köröttelijältä meni aikaa 4 tuntia 30 minuuttia.