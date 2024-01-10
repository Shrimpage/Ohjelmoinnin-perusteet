def omafunktio(arvo_parametrina): # parametrina arvo. syntyy kopio muuttujasta
    arvo_parametrina = 300
    return arvo_parametrina

def tokafunktio(lista_parametrina : list): # Parametrina viittaus listaan. syntyy kopio viittausmuuttujasta
    lista_parametrina[2] = 100    

a1 = [1,2,3,4,5,6]

print(a1)

tokafunktio(a1)

print(a1)