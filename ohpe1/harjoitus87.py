#Ohjelmoi ohjelma, jolla voi luoda kokonaislukutaulukon,
#jonka solujen sisältönä on aina indeksin arvo kaksinkertaisena.

taulukko = []

solut = int(input("Anna alkiot"))

for i in range(0,solut):
    taulukko.append(i*2)
    
    
print(taulukko)    

#def jokatoinen():
#    return sum(taulukko[::2])
#    print("Joka toinen alkio yhteen laskettuna on:" + str(jokatoinen()))    

def jokatoinen():
    vika = taulukko.pop()
    taulukko.insert(0, vika)
    return sum(taulukko[::2])
    
print("Joka toinen alkio yhteen laskettuna on:" + str(jokatoinen()))    
print(taulukko)