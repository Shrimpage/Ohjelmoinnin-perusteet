#Ohjelma joka kysyy kuinka suuri ryhmä on tulossa gondoli hissiin
luku = input("Kuinka monta henkilöä on tulossa hissiin? ")
tays = int(luku)//8
yli = (int(luku)/8-int(tays))*8
print("Ryhmä täyttää " + str(tays) + " hissiä, ja viimeiseen hissiin menee " + str(yli) + " henkilöä")