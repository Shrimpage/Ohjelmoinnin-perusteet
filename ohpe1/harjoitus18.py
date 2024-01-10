#ohjelma tulostaa kahdesta annetusta luvusta </>/=
n1 = input("Anna luku 1. ")
n2 = input("Anna luku 2. ")
if n1 == n2:
    print("Luvut ovat yhtä suuria.")
else:
    print("Luvut ovat eri suuria.")
    if n1 > n2:
        print("Luku 1. on suurempi kuin luku 2.")
    else:
        print("Luku 2. on suurempi kuin luku 1.")