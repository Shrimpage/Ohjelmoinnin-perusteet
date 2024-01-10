#kysyy käyttäjältä luvun ja tulostaa sen kaksinkertaisena.

def KahdellaKertominen():
    luku = int(input("Anna luku joka kerrotaan kahdella. "))
    print("2 * {0} = {1}".format(luku, (2*luku)))

KahdellaKertominen()