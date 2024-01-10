print("Kuusen piirto ohjelma.")

kork = int(input("Kuinka korkean kuusen haluat? "))
taulukko = []

for i in range (0,kork):
    taulukko.append("")

for i in range (0,kork):
    taulukko.pop(0)
    taulukko.append("*")
    print(*taulukko)
    