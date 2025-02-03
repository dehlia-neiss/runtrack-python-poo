class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT}€")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.calculerPrixTTC()}€")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.calculerPrixTTC()


produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Smartphone", 500, 10)
produit3 = Produit("Tablette", 300, 15)


print("Produit 1 :")
produit1.afficher()
print("\nProduit 2 :")
produit2.afficher()
print("\nProduit 3 :")
produit3.afficher()


produit1.modifierNom("Ordinateur Portable")
produit1.modifierPrix(1200)

produit2.modifierNom("Smartphone Pro")
produit2.modifierPrix(600)

produit3.modifierNom("Tablette 10 pouces")
produit3.modifierPrix(350)


print("\nAprès modification :")
print("Produit 1 :")
produit1.afficher()
print("\nProduit 2 :")
produit2.afficher()
print("\nProduit 3 :")
produit3.afficher()
