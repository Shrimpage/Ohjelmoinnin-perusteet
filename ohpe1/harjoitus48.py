#kertotauluohjelma

import random
x = random.randint(1,10)
y = random.randint(1,10)

print("Ohjelma kysyy sinulta kertotauluja.")
oikein = 0
väärin = 0
i = 1

while i !=0:
    tulos = int(input("Laske {0} * {1} : ".format(x,y)))
    if tulos == (x*y):
        print("Oikein!!!")
        oikein += 1
    else:
        print("Väärin! Oikea vastaus oli {0}!".format(x*y))
        väärin += 1
    jatko = str(input("Jatketaanko? (K=kyllä, muut vastaukset lopettavat.)"))
    if jatko != "K":
        break
    else:
        pass
print("Sinä sait {0} laskua oikein ja {1} laskua väärin.".format(oikein,väärin))