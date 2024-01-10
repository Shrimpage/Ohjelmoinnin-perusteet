#sarjana tehtyjen mittausten tutkimista
mittaukset = int(input("Montako mittausta otettiin? "))
keskiarvo = float(0)
for i in range (1,1+int(mittaukset)):
    luku = float(input("Anna {0}. mittaus tulos: ".format(i)))
    keskiarvo += luku
    if i == 1:
        pienin = float(luku)
        suurin = float(luku)
    else:
        if luku < pienin:
            pienin = luku
        elif luku > suurin:
            suurin = luku
        else:
            pass
    
print("Mittauksia oli {0} kpl.\nPienin arvo {1}.\n Suurin arvo {2}.\n Keskiarvo {3}.".format(mittaukset,pienin,suurin,keskiarvo/mittaukset))        