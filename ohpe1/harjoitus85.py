#
import random

#1. Määrittele taulukko luvut, jossa on 27 kokonaislukua.
luvut = []
for i in range(27):
    luvut.append(random.randint(0,100))
print(luvut)

#2.Määrittele taulukko, jossa on neljä solua ja kaikkien solujen arvona on true.
solut = [True, True, True, True]
print(solut)

#3.Määrittele taulukko, johon kysytään ihmisten nimiä-
nimet = []
jatko = "k"
while jatko == "k":
    nimet.append(input("Anna nimi: "))
    jatko = input("Jatketaanko (k/e)?")
print(*nimet) #* eteen jos halutaan tulostaa pelkkä sisältö

#4.Kirjoita lauseet, joilla tulostat tauluko hölkynKölkyn sisällön. Rivi per solu.
holkynKolkyn = ["dfkee", "asdf", "jotain", "hjetrh"]
for rivi in holkynKolkyn:
    print(rivi)

#5. Kirjoita lauseet, joilla tulostat taulukon hölkynKölkyn ekan solun sisällön.
print("eka solu: " + holkynKolkyn[0])

#6. Kirjoita lauseet, joilla tulostat taulukon hölkynKölkyn viimeisen solun sisällön.
print("viimeinen solu: " + holkynKolkyn[-1])

#7. Määrittele taulukko, jossa on luvut-taulukon arvot float-tyyppisenä.
luvut2 = []
for rivi in luvut:
    luvut2.append(float(rivi))
print(luvut2)