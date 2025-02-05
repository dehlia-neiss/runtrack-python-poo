class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = "enzo"

animal = Animal()
print(f"L'âge de l'animal = {animal.age}")

animal.vieillir()
print(f"L'âge de l'animal = {animal.age}")


print(f"l'animal s'apelle = {animal.prenom}")