class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Prix : {self.prix}€")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")
    

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue


voiture1 = Voiture("Toyota", "Corolla", 2022, 25000)
voiture1.informationsVehicule()


moto1 = Moto("Yamaha", "MT-07", 2023, 7500)
moto1.informationsVehicule()

