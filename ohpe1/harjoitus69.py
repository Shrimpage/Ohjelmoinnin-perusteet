#Ohjelmoi metodi, joka saa parametrinaan tuotteen verottoman hinnan 
#ja alv-prosentin. Metodi palauttaa pääohjelmalle alv:n sisältävän hinnan. 
#Pääohjelma tulostaa verottoman hinnan, alv:n osuuden ja verollisen hinnan.

def metodi(veroton,prossa):
    return veroton * (prossa/100+1)
    
veroton = float(input("Annna veroton hinta: "))
prossa = float(input("Anna alv-prosentti: ")) 

tulos = metodi(veroton,prossa)  

print("Veroton hinta: {0:.2f} euroa. \nAlv:n osuus: {1:.2f} euroa. \nVerollinen hinta: {2:.2f} euroa.".format(veroton,tulos-veroton,tulos))