#muunnostaulukko tuumista senteiksi.
print("Tämä ohjelma tulostaa muunnostaulukon tuumista senteiksi halutulta väliltä.")
x = int(input("\nAnna tuumamitta josta aloitetaan: "))
y = int(input("\nAnna tuumamitta johon lopetetaan: "))
print("Muunnostaulukko:")
for i in range (int(x),int(y)+1):
    print("{0}¨     {1:.2f} cm".format(i,i*2.54))