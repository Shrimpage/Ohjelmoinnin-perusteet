#kertotaulun opetusohjelma
laskut = int(input("Montako laskutehtävää haluat?"))
oikein = 0
väärin = 0

for i in range(laskut):

    import random
    x = random.randint(1,10)
    y = random.randint(1,10)
    
    tulos = int(input("Laske {0} * {1} : ".format(x,y)))
    
    if tulos == (x*y):
        print("Oikein!!!")
        oikein += 1
    else:
        print("Väärin! Oikea vastaus oli {0}!".format(x*y))
        väärin += 1
print("Sinä sait {0} laskua oikein ja {1} laskua väärin.".format(oikein,väärin))