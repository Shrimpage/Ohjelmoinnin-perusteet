# Koodaa ohjelma ristinolla -pelin pelaamista varten. 
# Tee funktio lisaa_siirto(), joka saa parametreinaan pelilaudan (kaksiolotteinen taulukko), koordinaatit ja asetettavan merkin (O tai X). 
# Tarkista funktiossa onko haluttu paikka vapaana ja palauta funktiosta tieto onnistuiko siirto.
# Tee toinen funktio tarkista_tilanne(), joka saa parametrina pelilaudan ja tarkistaa löytyykö voittaja.
# Peli päättyy tasapeliin, jos lisää siirtoja ei voi tehdä.

print("Ristinolla peli.")
lauta = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
def lisaa_siirto(lauta,rivi,sarake,merkki):
        if lauta[rivi][sarake] == " ":
            lauta[rivi][sarake] = (merkki)
            tarkista_tilanne(lauta)
            
        else:
            print("Siinä kohdassa on jo merkki! Anna uusi siirto") 

def tarkista_tilanne(lauta):
    
    if lauta[0][0] == lauta[0][1] and lauta[0][1] == lauta[0][2] and lauta[0][0] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[0][0]))
        for alilista in lauta:
            print(alilista)
        wait = input("Paina näppäintä lopettaaksesi pelin")   
        exit()
    elif lauta[1][0] == lauta[1][1] and lauta[1][1] == lauta[1][2] and lauta[1][0] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[1][0]))
        for alilista in lauta:
            print(alilista)
        wait = input("Paina näppäintä lopettaaksesi pelin")   
        exit()
    elif lauta[2][0] == lauta[2][1] and lauta[2][1] == lauta[2][2] and lauta[2][0] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[2][0]))
        for alilista in lauta:
            print(alilista)
        wait = input("Paina näppäintä lopettaaksesi pelin")   
        exit()
    elif lauta[0][0] == lauta[1][0] and lauta[1][0] == lauta[2][0] and lauta[0][0] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[0][0]))
        for alilista in lauta:
            print(alilista)
        exit()
    elif lauta[0][1] == lauta[1][1] and lauta[1][1] == lauta[2][1] and lauta[0][1] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[0][1]))
        for alilista in lauta:
            print(alilista)
        wait = input("Paina näppäintä lopettaaksesi pelin")   
        exit()    
    elif lauta[0][2] == lauta[1][2] and lauta[1][2] == lauta[2][2] and lauta[0][2] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[0][2]))
        for alilista in lauta:
            print(alilista)
        wait = input("Paina näppäintä lopettaaksesi pelin")   
        exit()
    elif lauta[0][0] == lauta[1][1] and lauta[1][1] == lauta[2][2] and lauta[0][0] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[0][0]))
        for alilista in lauta:
            print(alilista)
        wait = input("Paina näppäintä lopettaaksesi pelin")   
        exit()
    elif lauta[2][0] == lauta[1][1] and lauta[1][1] == lauta[0][2] and lauta[2][0] != " ":
        print("Pelaaja {0} voitti!!!".format(lauta[2][0]))
        for alilista in lauta:
            print(alilista)
        wait = input("Paina näppäintä lopettaaksesi pelin")    
        exit()     
    elif lauta[0][0] != " " and lauta[0][1] != " " and lauta[0][2] != " " and lauta[1][0] != " " and lauta[1][1] != " " and lauta[1][2] != " " and lauta[2][0] != " " and lauta[2][1] != " " and lauta[2][2] != " ":
        print("Ei enää siirtoja! Peli päättyy tasapeliin")
        wait = input("Paina näppäintä lopettaaksesi pelin")   
        exit()
           

def main():
    while True:
        print("Pelilauta näyttää tältä:")
        for alilista in lauta:
            print(alilista)
        
        merkki = str(input("Anna laudalle laitettava merkki.(X tai O): "))

        rivi = int(input("Mille riville merkki laitetaan? 0=ylin, 1=keskimmäinen, 2=alin: "))

        sarake = int(input("Mille sarakkeelle merkki laitetaan? 0=vasen, 1=keskimmäinen, 2=oikea: "))

        lisaa_siirto(lauta,rivi,sarake,merkki)
       

if __name__ == '__main__':
    main()        