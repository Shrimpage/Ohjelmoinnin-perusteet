#ohjelma, joka osaa muuntaa Celsius-asteet Fahrenheit-asteiksi ja päinvastoin.

def Fasteet():
    asteet = float(input("Anna Celsius asteet: "))
    print("{0:.2f}° Celsiusta on {1:.2f}° Fahrenheittia".format(asteet,asteet*1.8+32))
    return
def Casteet():
    asteet = float(input("Anna Fahrenheit asteet: "))
    print("{0:.2f}° Fahrenheittia on {1:.2f}° Celsiusta".format(asteet,(asteet-32)*5/9))
    return

valikko = str(input("Lämpöasteiden muunnos.\n1 = Celsiukset Fahrenheiteiksi\n2 = Fahrenheitit Celsiuksiksi\n0 = Lopetus\n"))

if valikko == str("1"):
    Fasteet()

elif valikko == str("2"):
    Casteet()

elif valikko == str("0"):
    pass