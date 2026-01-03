#klasa = szablon , przepis
class Czlowiek:
    #istota
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie
        # adam.imie = "Adam"
        # ewa.imie = "Ewa"
#Powstanie obiektu
#Gotowanie z przepisu
adam = Czlowiek("Adam")
ewa = Czlowiek('Ewa')
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)