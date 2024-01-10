#tentti2

def main():
    while True:
        print("Tämä ohjelma laskee konttaukseen käytetyn kokonaisajan perusteella saatavat kokonaispisteet.")
        aika = float(input("Anna ensimmäisen ohjelman antama kokonaisaika: "))
        if aika < 0:
            print("Aika ei voi olla alle 0 sekuntia!!")
        elif aika <= 60:
            pisteet = (aika*0.8)
            if pisteet <= 20:
                print("Ajasta {0:.1f} vähennettiin 20% ja sait ajan {1:.1f}, joka on 5 pistettä!".format(aika, pisteet))
                break
            elif pisteet <= 30:
                print("Ajasta {0:.1f} vähennettiin 20% ja sait ajan {1:.1f}, joka on 4 pistettä!".format(aika, pisteet))
                break                
            elif pisteet <= 40:
                print("Ajasta {0:.1f} vähennettiin 20% ja sait ajan {1:.1f}, joka on 3 pistettä!".format(aika, pisteet))
                break
            elif pisteet <= 50:
                print("Ajasta {0:.1f} vähennettiin 20% ja sait ajan {1:.1f}, joka on 2 pistettä!".format(aika, pisteet))
                break
            else:
                print("Ajasta {0:.1f} vähennettiin 20% ja sait ajan {1:.1f}, joka on 1 pistettä!".format(aika, pisteet))
                break               
        else:
            print("Aikasi oli yli minuutin, joten et saanut pisteitä.")
            break
        
if __name__ == '__main__':
    main()