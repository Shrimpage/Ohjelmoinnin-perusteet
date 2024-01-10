#Ohjelma joka muuntaa Fahrenheit-asteet Celsius-asteiksi
print("Tämä ohjelma muuntaa lämpötilan Fahrenheit-asteista Celsius-asteiksi.")
fah = input("Anna lämpötila Fahrenheit-asteina: ")
C = 5*(float(fah)-32)/9
print("Lämpötilä Celsius-asteina: " +str(C))