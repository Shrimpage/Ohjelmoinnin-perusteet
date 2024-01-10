#ohjelma tulostaa kokeen arvosanan pistemäärän avulla.
print("Tämä ohjelma selvittää kokeesi arvosanan.")
pisteet = input("Anna pistemääräsi (0-60): ")
if int(pisteet) < 11:
    print("Arvosanasi on 0!")
elif int(pisteet) >10 and int(pisteet) < 21:
    print("Arvosanasi on 1!")
elif int(pisteet) >20 and int(pisteet) < 31:
    print("Arvosanasi on 2!")
elif int(pisteet) >30 and int(pisteet) < 41:
    print("Arvosanasi on 3!")
elif int(pisteet) >40 and int(pisteet) < 51:
    print("Arvosanasi on 4!")    
else:
    print("Arvosanasi on 5!")    