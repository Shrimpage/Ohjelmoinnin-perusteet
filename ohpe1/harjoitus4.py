#Ohjelma laskee taksimatkan hinnan
print("Tämä ohjelma laskee taksimatkasi hinnan.")

lähtöhinta = input("Paljonko matkan lähtöhinta oli? ")
kilometrihinta = input("Paljonko matkan kilometrihinta oli? ")
matkakilometreinä = input("kuinka pitkä matka oli kilometrin tarkkuudella? ")
hinta = float(lähtöhinta) + float(kilometrihinta) * float(matkakilometreinä)

print("Matkan kokonais hinta oli: " + str(hinta))