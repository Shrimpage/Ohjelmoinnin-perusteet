#Ohjelma kysyy alimmat ja ylimmät sademäärät halutulta ajalta ja laskee niiden keskiarvon.
print("Tämä ohjelma laskee halutun ajan sademäärien keskiarvon. ")
y = int(input("Kuinka monen päivän sademäärät haluat laskea? "))
keski = 0
for x in range (1,int(y)+1):
    sade = float(input("\nAnna päivän {0}. sademäärä mm: ".format(x)))
    keski = float(keski) + float(sade)
print("\nViikon keskimääräinen sademäärä on {0:.1f} mm. ".format(keski/7))