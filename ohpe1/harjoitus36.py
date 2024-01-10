#Ohjelma kysyy lämpötilat viikon ajalta ja laskee niiden keskiarvon.
print("Tämä ohjelma laskee viikon lämpötiojen keskiarvon. ")
keski = 0
for x in range (1,8):
    lämpö = float(input("Anna päivän {0} lämpötila °C: ".format(x)))
    keski = float(keski) + float(lämpö)
print("Viikon lämpötilojen keskiarvo on {0:.1f} °C. ".format(keski/7))