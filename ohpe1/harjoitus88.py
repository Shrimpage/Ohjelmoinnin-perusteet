#Ohjelmoi ohjelma, jossa on taulukko, jonka sisältönä on seuraavat arvot:
#1, 11, 101, 1001, 10001, 100001. 
#Ohjelma pyytää käyttäjältä luvun ja ohjelma tulostaa taulukon indeksin, 
#josta löytyy lähin annettua lukua suurempi luku. Ohjelman on sisällettävä toisto-toiminto.

taulukko = [1,11,101,1001,10001,100001]

def tarkastelu():
    luku = int(input("Anna tarkasteltava luku: "))
    if luku < 1:
        index = taulukko.index(1)
        print("Tarkasteltavaa lukua {0} lähin suurempi luku löytyy listasta indexillä {1}.".format(luku,index))
        return 
    elif luku < 11:
        index = taulukko.index(11)
        print("Tarkasteltavaa lukua {0} lähin suurempi luku löytyy listasta indexillä {1}.".format(luku,index))
        return
    elif luku < 101:
        index = taulukko.index(101)
        print("Tarkasteltavaa lukua {0} lähin suurempi luku löytyy listasta indexillä {1}.".format(luku,index))
        return
    elif luku < 1001:
        index = taulukko.index(1001)
        print("Tarkasteltavaa lukua {0} lähin suurempi luku löytyy listasta indexillä {1}.".format(luku,index))
        return
    elif luku < 10001:
        index = taulukko.index(10001)
        print("Tarkasteltavaa lukua {0} lähin suurempi luku löytyy listasta indexillä {1}.".format(luku,index))
        return
    elif luku < 100001:
        index = taulukko.index(100001)
        print("Tarkasteltavaa lukua {0} lähin suurempi luku löytyy listasta indexillä {1}.".format(luku,index))
        return    
    else:
        print("Tarkasteltavaa lukua {0} suurempaa lukua ei löydy tästä taulukosta.".format(luku))
        return    
        
        
def main():
    while True:
        print(taulukko)
        print("Ohjelma tarkastelee käyttäjän antamaa lukua")
        print("1 = Käynnistä ohjelma")
        print("0 = Lopetus")
        valinta = int(input("Valinta: "))
        
        if valinta == 1:
            tarkastelu()
        elif valinta == 0:
            break
        else:
            print("Virheellinen valinta")
            
if __name__ == '__main__':
    main()