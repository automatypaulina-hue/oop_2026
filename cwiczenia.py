# Napisz klasę FiguraGeometryczna, która będzie zawierała
# metody:
# policz_pole()
# policz_obwód()

# Napisz klasy Prostokąt, Kwadrat, Koło i Trojkat
# oraz zaimplementuj metody z interfejsu FiguraGeometryczna

# Stwórz instancje tych klas i sprawdź ich działanie


# Klasa bazowa (interfejs)
from abc import ABC, abstractmethod


class FiguraGeometryczna(ABC):

    @abstractmethod
    def policz_pole(self):
        """Metoda do obliczenia pola figury."""
        pass

    @abstractmethod
    def policz_obwod(self):
        """Metoda do obliczenia obwodu figury."""
        pass


# Prostokąt
class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def policz_pole(self):
        return self.a * self.b

    def policz_obwod(self):
        return 2 * (self.a + self.b)


# Kwadrat
class Kwadrat(FiguraGeometryczna):
    def __init__(self, a):
        self.a = a

    def policz_pole(self):
        return self.a * self.a

    def policz_obwod(self):
        return 4 * self.a


# Koło
import math  # Dodajemy import modułu math

class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r

    def policz_pole(self):
        return math.pi * self.r * self.r

    def policz_obwod(self):
        return 2 * math.pi * self.r



# Trójkąt (zakładamy zwykły trójkąt o bokach a, b, c)
class Trojkat(FiguraGeometryczna):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h  # wysokość do boku a

    def policz_pole(self):
        return (self.a * self.h) / 2

    def policz_obwod(self):
        return self.a + self.b + self.c



prostokat = Prostokat(4, 6)
kwadrat = Kwadrat(5)
kolo = Kolo(3)
trojkat = Trojkat(3, 4, 5, 4)

figury = [prostokat, kwadrat, kolo, trojkat]

for figura in figury:
    print(type(figura).__name__)
    print("Pole:", figura.policz_pole())
    print("Obwód:", figura.policz_obwod())
    print("-------------------")
