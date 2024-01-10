# Tee ohjelma englannin kielen sanojen kyselyä varten. Sijoita ohjelmassa Dictionary-rakenteeseen sanoja. 
# Arvo indeksi, mistä kysyttävä sana otetaan ja tulosta kysymys. Lisää laskurit oikeille ja väärille vastauksille.
# Kysy silmukassa kymmenen sanaa, tarkista tulos ja tulosta lopuksi montako meni oikein.
# Vinkki: Dictionaryn alkioon ei voi viitata suoraan indeksillä, vaan tarvitaan avain. 
# Avainkentät saa kuitenkin rakenteesta ulos käyttämällä metodia keys() eli esimerkiksi näin: avaimet_listana = list(oma_sanakirja.keys()) 

print("Tämä ohjelma kyselee englannin kielen sanoja ja laskee oikeat sekä väärät arvaukset. ")

import random

oikein = 0
vaarin = 0

oma_sanakirja = {
"kaide" : "railing",
"parantaa" : "mend",
"oleellinen" : "essential",
"haukotella" : "yawn",
"suistua" : "swerve",
"kostea" : "moist",
"jono" : "queue",
"väliaikainen" : "temporary",
"tahra" : "stain",
"itsepäinen" : "stubborn",
"kömpelö" : "clumsy",
"yksinomaan" : "exclusively",
"katua" : "regret",
"epävarma" : "insecure",
"arpajaiset" : "raffle",
"surkea" : "lousy",
"solmu" : "knot",
"lehmä" : "cow",
"omena" : "apple",
"aurinko" : "sun",
"näppäimistö" : "keyboard"
}


avaimet_listana = list(oma_sanakirja.keys())


satunnaiset = []

while len(satunnaiset) < 10:
    arvo = random.randint(0,20)
    sana = avaimet_listana[arvo]
    if satunnaiset.count(sana) < 1:
        satunnaiset.append(sana)
        arvaus = str(input("Sana {0} on englanniksi? ".format(sana))).lower()
        if arvaus == (oma_sanakirja[sana]):
            print("Oikein!")
            oikein += 1
        else:
            print("Väärin!")
            vaarin += 1

loppu = input("Testi loppui. Sait {0} oikein ja {1} väärin.".format(oikein,vaarin))