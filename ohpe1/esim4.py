#

def Summa(eka, toka):
    return eka + toka
    
def Erotus(eka, toka):
    return eka - toka

def Tulo(eka, toka):
    return eka * toka

def Osamaara(eka, toka):
    return eka / toka    

def Laskin(luku1, oper, luku2):
    if oper == "+":
        tulos = Summa(luku1, luku2)
        return tulos
    elif oper == "-":
        tulos = Erotus(luku1, luku2)
        return tulos
    elif oper == "*":
        tulos = Tulo(luku1, luku2)
        return tulos
    elif oper == "/":
        tulos = Osamaara(luku1, luku2)
        return tulos
        
def main():        
        
    luku1 = int(input("Anna eka luku: "))
    oper = str(input("Anna laskutoimitus: "))
    luku2 = int(input("Anna toka luku: "))

    print("Tulos on: " + str(Laskin(luku1, oper, luku2)))

if __name__== '__main__':
    main()