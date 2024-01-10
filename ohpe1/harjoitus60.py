#tulostaa parametrina saamansa luvun kolminkertaisena.

def KolmellaKertominen(luku):
    print("{0} * 3 = {1}.".format(luku,luku*3))


KolmellaKertominen(int(input("Anna kolmella kerrottava luku: ")))
