#
#karkausvuosien tarkastelua
print("Ohjelma selvittää onko antama vuosi karkausvuosi.")

i = int(0)
while i < 1:
    vuosi = int(input("Anna tarkasteltava vuosi. (vuosi 0 lopettaa ohjelman)"))
        
    if vuosi == int(0):
        break
    elif (vuosi % 4) == 0 and (vuosi % 100) != 0 or (vuosi % 400) ==0:
        print("Vuosi {0} on karkausvuosi.".format(vuosi))
    elif (vuosi % 400) == 0:
        print("Vuosi {0} on karkausvuosi.".format(vuosi))
    else:
        print("Vuosi {0} ei ole karkausvuosi.".format(vuosi))
