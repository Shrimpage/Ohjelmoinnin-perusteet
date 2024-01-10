#ohjelma antaa laitteen asetukset kahden mittarituloksen perusteella.
print("Tämä ohjelma kertoo laitteen asetuksen mittareiden arvojen perusteella.")
mittari1 = int(input("Anna mittarin 1 arvo (1-10): "))
mittari2 = input("Anna mittarin 2 arvo (L,M tai H): ")
if mittari1 >= 0 and mittari1 <= 3:
    if mittari2 == str("H"):
        print("Laitteen asetus on 2.")
    elif mittari2 == str("L") or mittari2 == str("M"):
        print("Laitteen asetus on 1.")   
    else:
        print("Mittausvirhe!!!")
elif mittari1 >= 4 and mittari1 <= 7:
    if mittari2 == str("L"):
        print("Laitteen asetus on 2.")
    elif mittari2 == str("H") or mittari2 == str("M"):
        print("Laitteen asetus on 3.")   
    else:
        print("Mittausvirhe!!!")
elif mittari1 >= 8 and mittari1 <= 10:
    if mittari2 == str("L"):
        print("Laitteen asetus on 3.")
    elif mittari2 == str("H") or mittari2 == str("M"):
        print("Laitteen asetus on 4.")   
    else:
        print("Mittausvirhe!!!")   
else:
    print("Mittausvirhe!!!")