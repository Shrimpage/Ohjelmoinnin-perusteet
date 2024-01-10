#3.	Laadi ohjelma, joka laskee kuinka moni sai hyvitystä aikaansa (=aika oli alle minuutin) 
# ja kuinka moni ei saanut hyvitystä sekä aikojen keskiarvon. 
# Ohjelmassa on toisto, joka jatkuu niin kauan kunnes ajaksi annetaan nolla. 
# Ohjelma kysyy joka kierroksella ajan ja summaa aikojen yhteismäärää sekä  joko hyvityksen 
# saaneiden lukumäärää tai hyvitystä saamattomien lukumäärää. 
# Ohjelma tulostaa lopuksi kuinka moni sai hyvitystä ja kuinka moni ei ja mikä oli 
# aikojen keskiarvo.

print("Tämä ohjelma laskee kuinka moni sai hyvitystä aikaansa sekä aikojen keskiarvon.")



def main():
    keskiarvo = 0
    hyvitys = 0
    luku = 0
    lukusai = 0
    lukuei = 0
    while True:
        aika = float(input("Anna aika. (0 lopettaa toiston): "))
        if aika < 0:
            print("Aika ei voi olla negatiivinen!")
        elif aika > 0 and aika < 60:
            keskiarvo += aika
            hyvitys += 1
            lukusai += 1
        elif aika == 0:
            keskiarvo = (keskiarvo/(lukusai+lukuei))
            print("Kaikkien aikojen keskiarvo oli {0:.1f} sekuntia. Hyvitystä saaneita oli {1} ja niitä jotka eivät saaneet hyvitystä oli {2}.".format(keskiarvo, lukusai, lukuei))
            break
        else:
            keskiarvo += aika
            lukuei += 1
    
    
if __name__ == '__main__':
    main()
