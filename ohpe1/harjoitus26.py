#yksinkertainen laskukone
print ("Tämä on yksinkertainen laskin:")
a = float(input("Anna 1. luku: "))
b = float(input("Anna 2. luku: "))
ope = str(input("Anna laskun operaattori (+,-,*,^,/): "))
if str(ope) == "+":
    tulos = (a + b)
    print("Ratkaisu on " + str(tulos) +".")
elif str(ope) == "-":
    tulos = (a - b)
    print("Ratkaisu on " + str(tulos) +".")
elif str(ope) == "*":
    tulos = (a * b)
    print("Ratkaisu on " + str(tulos) +".")
elif str(ope) == "^":
    tulos = (a ** b)
    print("Ratkaisu on " + str(tulos) +".")
elif str(ope) == "/":
    tulos = (a / b)
    print("Ratkaisu on " + str(tulos) +".")
else:
    print("Käyttäjä olikin yksinkertaisempi kuin laskin.")