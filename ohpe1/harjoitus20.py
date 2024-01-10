#porrasverokortti
palkka = input("Paljonko saat nettopalkkaa? ")
ennakko = input("Paljonko ennakonpidätysprosenttisi on? ")
raja = input("Kuinka suuri on tuloraja tälle prosentille? ")
lisä = input("Paljonko ennakonpidätysprosenttisi on tulorajan ylittävästä osasta? ")
if float(palkka) <= float(raja):
    raha = float(palkka)-(float(palkka)*float(ennakko)/100)
    print("Palkasta jää käteen {0:.2f} euroa.".format(raha))
else:
    raha1 = float(raja)*float(ennakko)/100
    raha2 = (float(palkka)-float(raja))*float(lisä)/100
    raha = float(palkka)-float(raha1)-float(raha2)
    print("Palkasta jää käteen {0:.2f} euroa.".format(raha))