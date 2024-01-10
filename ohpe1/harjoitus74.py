

def kertoma(luku):
    kertoma = 1
    for i in range (0,luku):
        kertoma = kertoma*(i+1)
    return kertoma    
    
luku = int(input("Anna luku, niin ohjelma laskee sen kertoman: "))
print(kertoma(luku))