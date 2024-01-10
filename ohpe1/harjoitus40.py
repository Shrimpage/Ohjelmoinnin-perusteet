#viikon kuntopisteiden laskenta ohjelma.
kävely = 0
juoksu = 0
hiihto = 0
uinti = 0
print("Tämä ohjelma laskee viikkosi kuntopisteet.\nIlmoita urheilusuorituksen laji kirjaimella:\nKävely=k\nJuoksu=j\nHiihto=h\nUinti=u")
for i in range (1,8):
    laji = input("Anna päivän {0} urheilusuorituksen laji: ".format(i))
    if str(laji) == str("k"):
        kävely += float(input("Anna kävelty matka kilometreinä: "))
    elif laji == str("j"):
        juoksu += float(input("Anna juostu matka kilometreinä: "))
    elif laji == str("h"):
        hiihto += float(input("Anna hiihdetty matka kilometreinä: "))
    elif laji == str("u"):
        uinti += float(input("Anna uitu matka kilometreinä: "))
    else:
        print("Tuntematon laji! Ei suoritusta päivältä {0}! ".format(i))
print("Viikon kuntopisteet: ")
print("Kävely: {0}\nJuoksu: {1}\nHiihto: {2}\nUinti: {3}".format(kävely,juoksu*2,hiihto*3,uinti*5))        