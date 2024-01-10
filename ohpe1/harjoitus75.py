#Ohjelmoi metodi, joka tulostaa parametrina saamansa merkin parillisille riveille ja
#toisen parametrina saamansa merkin parittomille riveille. 
#Rivien määrä ja pituus tulevat  myös parametreina.

def metodi(merkki1, merkki2, maara, pituus):
    for i in range (0, pituus):
        
        if i % 2 == 0:
            for i in range (0, maara):
                print(str(merkki1), end ="")
            print("")
        else:
            for i in range (0, maara):
                print(str(merkki2), end ="")
            print("")    
                




merkki1 = str(input("Anna ensimmäinen merkki: "))
merkki2 = str(input("Anna toinen merkki: "))
maara = int(input("Kuinka monta kertaa merkit tulostetaan riville? "))
pituus = int(input("Kuinka monta riviä tulostetaan? "))

metodi(merkki1, merkki2, maara, pituus)