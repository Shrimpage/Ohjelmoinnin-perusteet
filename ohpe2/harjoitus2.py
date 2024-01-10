
nimi = "pappa"
ika = 76

oma_lista = [nimi,ika]
oma_tuple = (nimi,ika)

print("nimi:", oma_tuple[0])
print("ikä:", oma_tuple[1])

(nimi2, ika2) = oma_tuple

ika2 =34

oma_tuple = (nimi2, ika2)
toka_tuple = ("Pekka", 36)

oma_tuple = oma_tuple + toka_tuple

print("nimi:", oma_tuple[0])
print("ikä:", oma_tuple[1])
print("nimi:", oma_tuple[2])
print("ikä:", oma_tuple[3])

for i in oma_tuple:
    print(i)

print(oma_tuple.count(36))

print(oma_tuple.index(36))