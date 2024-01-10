#Tee ohjelma, jossa määritellään tuotekoodit ja niitä vastaavat tuotenimet.
#Ohjelma sisältää metodin, joka palauttaa parametrina annettua tuotekoodia vastaavan nimen. 
#Voit ratkaista ohjelman joko käyttäen kahta yksiulotteista taulukkoa tai yhtä kaksiulotteista taulukkoa.

koodit = [501,402,303,204,105]
tuotteet = ["omena","banaani","kiivi","mango","appelsiini"]

print(koodit)

def palautus(koodi):
    if koodi in koodit:
        index = int(koodit.index(koodi))
        return tuotteet[index]
        
koodi = int(input("Anna etsittävä tuotekoodi listasta, niin ohjelma etsii ja tulostaa sitä vastaavan tuotteen. "))
print(palautus(koodi))
