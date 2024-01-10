# kysyy käyttäjältä palan tekstiä ja tulostaa tekstin yhdellä rivillä itseensä katenoituna (=liitetään perään sama teksti).

def Katenointi():
    teksti = str(input("Anna teksti joka katenoidaan: "))
    print(teksti + teksti)

Katenointi()