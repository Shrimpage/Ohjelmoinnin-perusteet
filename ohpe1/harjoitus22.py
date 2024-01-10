#ohjelma laskee asunnonvälittäjän palkkion
print ("Tämä ohjelma laskee kuinka paljon asunnonvälittäjä perii palkkiota sen ollessa 5%.")
summa = input("Paljonko asunnon myyntihinta oli? ")
palkkio = float(summa) * 0.05
if float(palkkio) < 2000:
    print("Palkkio on 2000 euroa.")
elif float(palkkio) > 15000:
    print("Palkkio on 15000 euroa.")
else:
    print("Palkkio on {0:.2f} euroa.".format(palkkio))