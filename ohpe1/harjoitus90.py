#Lottoriviohjelma

import random
i=0
l=0
maara=0
lottorivi = []

maara = int(input("Anna arvottavien lottolukujen määrä: "))
luku = int(input("Anna arvottavien lottorivien määrä: "))

while l < luku:
    i = 0
    l += 1
    while i < maara:
        a = random.randint(1,40)
        if a in lottorivi:
            pass
        else:
            lottorivi.append(a)
            i += 1
    print(lottorivi)
    lottorivi = []
    