#ohjelma tunnistaa onko kolmio suorakulmainen.
print("Anna kolmion sivut eri riveillä:")
c = input("Anna kolmion hypotenuusa: ") 
a = input("Anna kolmion kateetin pituus: ") 
b = input("Anna kolmion toisen kateetin pituus: ")
if float(c)*float(c)==float(a)*float(a)+float(b)*float(b):
    print("Kolmio on suorakulmainen!")
else:
    print("Kolmio ei ole suorakulmainen!")