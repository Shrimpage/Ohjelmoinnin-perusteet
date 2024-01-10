

def metodi(luku):
    summa = 0
    for i in range (0,luku):
        print("{0} + {1} = {2} ".format(summa,i+1,summa+i+1))
        summa += i+1
        
luku = int(input("Anna luku johon asti summaillaan: "))
metodi(luku)        