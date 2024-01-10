#Ohjelma kysyy alimmat ja ylimmät lämpötilat viikon ajalta ja laskee niiden keskimääräisen vaihteluvälin.
print("Tämä ohjelma laskee viikon lämpötiojen keskimääräisen vaihteluvälin. ")
keski = 0
for x in range (1,8):
    ylämpö = float(input("\nAnna päivän {0} ylin lämpötila °C: ".format(x)))
    alämpö = float(input("Anna päivän {0} alin lämpötila °C: ".format(x)))
    keski = float(keski) + float(ylämpö) - float(alämpö)
print("\nViikon lämpötilojen keskiarvoinen vaihteluväli on {0:.1f} °C. ".format(keski/7))