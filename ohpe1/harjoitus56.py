luku = int(input("Anna luku joka jaetaan tekijöihin: "))
print("Luvun {0} tekijät ovat: ".format(luku))
for i in range (0,luku):
    if luku % (i+1) == 0:
        print("{0} * {1}".format(i+1,luku/(i+1)))