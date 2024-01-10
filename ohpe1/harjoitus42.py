#karkausvuodet halutulta aikaväliltä.
print("Ohjelma laskee karkausvuodet halutulta vuosilukuväliltä:")
alku = int(input("Anna aloitettava vuosi: "))
loppu = int(input("Anna lopetettava vuosi: "))

if alku < loppu:
    print("Karkausvuodet tällä välillä: ")
    for i in range (alku,1+loppu):
        if (i % 4) == 0 and (i % 100) != 0:
            print("{0}".format(i))
        elif (i % 400) == 0:
            print("{0}".format(i))
        else:
            pass
else:
    print("Virhe vuosiluvuissa!")