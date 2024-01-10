#Ohjelmoi metodi, jolla voi tarkistaa mitatun kuumearvon järkevyyden. Kuumeen määrä annetaan parametrina.
#Metodi palauttaa true tai false.

def metodi(asteet):
    if asteet <= 32 or asteet >= 42 :
        return True
    else:
        return False
        
def main(): 
       
    asteet = float(input("Anna kuumemitttarin asteluku: "))

    if metodi(asteet):
        print("Mittari on rikki")
    else:
        print("Mittarin arvo on järkevä")
        
if __name__ == '__main__':
    main()