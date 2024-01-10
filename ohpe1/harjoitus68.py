#korkoa korolle

def KorkoaKorolle(saldo,korko,vuodet):
    return (saldo*(1+korko/100)**vuodet)

saldo = float(input("Anna sijoituksen saldo: "))
korko = float(input("Anna sijoituksen korko: "))
vuodet = float(input("Anna sijoituksen kesto vuodet: "))

print("Uusi saldo on {} euroa.".format(KorkoaKorolle(saldo,korko,vuodet)))