#Metodi tulostaa tekstin:
#Ohjelma on suorittanut virheen ---tähän parametrina tullut virhe----  ja se lopetetaan.

def Virheilmoitus(virhe):
    print("Ohjelma on suorittanut virheen ---{0}----  ja se lopetetaan.".format(virhe))

Virheilmoitus(input(""))
    