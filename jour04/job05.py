import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__largeur * self.__hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def aire(self):
        return math.pi * self.__radius ** 2

rectangle1 = Rectangle(10, 5)
cercle1 = Cercle(7)

print("Aire du rectangle :", rectangle1.aire())
print("Aire du cercle :", cercle1.aire())
