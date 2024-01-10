# Kirjoita luokka Opiskelijarekisteri, joka pitää tallessa opiskelijoiden tietoja (Esimerkiksi Dictionary-rakenteissa). 
# Luokalla on toiminnot opiskelijan tietojen lisäämiseksi ja hakemiseksi. 
# Opiskelijaa lisättäessä luokka antaa opiskelijalle opiskelijanumeroksi seuraavan vapaan numeron. 
# Ensimmäinen opiskelija saa opiskelijanumeroksi luvun 10000, seuraava 10001 jne. (hyödynnä luokan staattista muuttujaa).
# Opiskelijasta tallennettavia tietoja ovat opiskelijanumero, nimi, ryhmä ja opintopisteet. 
# Tallennusrakenne voi näyttää vaikkapa seuraavalta: {"10001": {"Nimi": "Heikki", "Ryhmä": "AUTE20", "Opintopisteet": 15}. 
# Hakutoiminnossa opiskelijan tiedot haetaan opiskelijanumeron perusteella.
# Voit myös lisätä toiminnon opiskelijoiden tietojen tallentamiseksi json-tiedostoon.

class Opiskelijarekisteri:
    opiskelija_id = 10000

    def __init__(self, nimi:str, ryhma:str, opisteet:int):
        Opiskelijarekisteri.opiskelija_id += 1
        self.__opiskelija = Opiskelijarekisteri
        self.__nimi = nimi
        self.__ryhma = ryhma
        self.__opisteet = opisteet
