#

#lasketaan joukkoeen pisteet ja tulostetaan

def metodi(osallistujat):
    total = 0
    for i in range (0,osallistujat):
        pisteet = int(input("Anna {0}. jäsenen pistemäärä: ".format(i+1)))
        total += pisteet
    return total   
        
#pääohjelma tulostaa otsikon, kysyy joukkoeet ja suorittaa toiston

def main():
    while True:
        print("SYYSKARKELOT!")
        joukkoeet = int(input("Montako joukkoetta osallistuu kisaan? "))
        for i in range (0,joukkoeet):
            nimi = input("Anna {0}. joukkoeen nimi: ".format(i+1))
            osallistujat = int(input("Anna osallistujamäärä: "))
            print("Joukkoe {0}: {1} pistettä.".format(nimi,metodi(osallistujat)))
        
        break    
    
if __name__ == '__main__':
    main()