#Ohjelmoi ohjelma, joka sisältää kuukausien nimet taulukossa. 
#Ohjelma kyselee kuukausien numeroita ja tulostaa kuukauden tekstinä (0 lopettaa).

kuukaudet = ["Tammikuu","Helmikuu","Maaliskuu","Huhtikuu","Toukokuu","Kesäkuu","Heinäkuu","Elokuu","Syyskuu","Lokakuu","Marraskuu","Joulukuu"]

def kuut(kuu):
    print(kuukaudet[kuu])
    return
    

def main():
    while True:
        print("Ohjelma tulostaa numeroa vastaavan kuukauden nimen taulukosta.")
        arvo = int(input("Anna kuukauden numero 1-12. (0 lopettaa ohjelman): "))
        
        if arvo >= 1 and arvo <=12:
           kuu = -1
           kuu += arvo
           kuut(kuu)
        elif arvo == 0:
            break
        else:
            print("Virheellinen arvo!!")
 
 
if __name__ == '__main__':
    main()