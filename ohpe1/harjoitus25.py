#ohjelma määrittelee kuuloaistin tason
db = int(input("Ohjelma ilmoittaa kuuloaistisi tason. \nIlmoita kuulokynnyksesi. (dB): "))
if db < 25:
    print("Ei alenemaa")
elif db >=25 and db <=40:
    print("Lievä alenema")
elif db >=41 and db <=55:
    print("Kohtalainen alenema")
elif db >=56 and db <=70:
    print("Keskivaikea alenema")
elif db >=71 and db <=90:
    print("Vaikea alenema")
else:
    print("Erittäin vaikea alenema")
    