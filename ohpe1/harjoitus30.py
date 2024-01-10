#ohjelma kysyyy 6 lukua ja kertoo niistä faktoja
a = int(input("Anna kokonaisluku a: "))
b = int(input("Anna kokonaisluku b: "))
c = int(input("Anna kokonaisluku c: "))
p = float(input("Anna desimaaliluku p: "))
q = float(input("Anna desimaaliluku q: "))
r = float(input("Anna desimaaliluku r: "))

print("Väittämä 1: \nJoko a on 7 ja b on negatiivinen tai q on suurempi kuin r:n ja p:n erotus: ")
if a == 7 and b > 0:
    print("Väittämä 1 on totta! ")
elif q > float(r)-float(p):
    print("Väittämä 1 on totta! ")
else:
    print("Väittämä 1 on tarua! ")
    
print("Väittämä 2: \nr < -1.7 tai r > 23.1, c:n ja a:n summa on parillinen ja b ei ole 538: ")
if r < -1.7 or r >23.1 and (int(a) + int(c)) % 2 != 0.5 and b != 538:
    print("Väittämä 2 on totta! ")
else:
    print("Väittämä 2 on tarua! ")

print("Väittämä 3: \nJoko a on 7 tai b on c, mutta ei molemmat: ")
if a == 7:
    if b != c:
        print("Väittämä 3 on totta! ")
    else:
        print("Väittämä 3 on tarua! ")
elif b == c:
    if a != 7:
        print("Väittämä 3 on totta! ")
    else:
        print("Väittämä 3 on tarua! ")
else:
    print("Väittämä 3 on tarua! ")
#joko a on 7 tai b on c, mutta ei molemmat
