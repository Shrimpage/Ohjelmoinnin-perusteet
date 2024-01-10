#vuosikilometrikorvaus
km = input("Tämä ohjelma laskee vuosikilometrikorvauksen määrän. Kuinka paljon ajoit tänä vuonna? ")
if float(km) < 5000 or float(km) == 5000:
    korvaus = float(km)*0.43
    print ("Vuosikilometrikorvauksesi on {0:.2f} euroa.".format(korvaus))
else:
    km2 = float(km)-5000
    korvaus = 5000*0.43 + float(km2)*0.30
    print ("Vuosikilometrikorvauksesi on {0:.2f} euroa.".format(korvaus))