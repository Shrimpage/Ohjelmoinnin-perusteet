#Ohjelmoi metodi, joka palauttaa kuukauden numeroa vastaavan tekstin. 
#Esimerkiksi 3 => maaliskuu.

def kuukausi(numero):
    
    if numero == str("1"):
        return str("tammikuu")
    elif numero == str("2"):
        return str("helmikuu")
    elif numero == str("3"):
        return str("maaliskuu")
    elif numero == str("4"):
        return str("huhtikuu")
    elif numero == str("5"):
        return str("toukokuu")
    elif numero == str("6"):
        return str("kesäkuu")
    elif numero == str("7"):
        return str("heinäkuu")
    elif numero == str("8"):
        return str("elokuu")
    elif numero == str("9"):
        return str("syyskuu")
    elif numero == str("10"):
        return str("lokakuu")
    elif numero == str("11"):
        return str("marraskuu")
    elif numero == str("12"):
        return str("joulukuu")
    else:
        return str("Ei vastaa kuukautta!")

numero = input("Anna numero 1-12: ")

print("{0} => {1}.".format(numero,kuukausi(numero)))