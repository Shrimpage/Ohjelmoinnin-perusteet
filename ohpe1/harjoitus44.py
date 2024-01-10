#lukujen kyselyä
i = 1
luku = 0

while luku >= 0:
    luku = int(input("Anna luku: "))
    i += 1
print("Ohjelma päättyy. Annoit negatiivisen luvun {0} ja se oli {1}. luku.".format(luku,i-1))    