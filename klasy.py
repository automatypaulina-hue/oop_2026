#klasa = szablon , przepis
class Czlowiek:
    #istota
    gatunek = "Homo Sapiens"
    def __init__(self):
        print("Niech powstanie czlowiek")
#Powstanie obiektu
#Gotowanie z przepisu
adam = Czlowiek()
#print(type(adam))
#print(dir(Czlowiek))
#print(dir(adam))
print(adam.gatunek)