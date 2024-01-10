#palauttaa tiedon, onko parametrina saatu luku jaollinen seiskalla vai ei.

def SeiskallaJaollinen(luku):
    if luku % 7 == 0:
        return True
    else:
        return False
        
luku = int(input("Anna luku: "))

if SeiskallaJaollinen(luku):
    print("Luku on seiskalla jaollinen.")
else:
    print("Luku ei ole seiskalla jaollinen.")