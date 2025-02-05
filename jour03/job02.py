class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def ajouter_habitant(self):
        self.__habitants += 1

    def get_habitants(self):
        return self.__habitants

    def get_nom(self):
        return self.__nom

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()

class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte N°{self.__numero} - Titulaire: {self.__nom} {self.__prenom} - Solde: {self.__solde}€")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde: {self.__solde}€")

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05 
            print(f"Agios appliqués. Nouveau solde: {self.__solde}€")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Virement impossible, fonds insuffisants.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ vers le compte {compte_destinataire.__numero} effectué.")


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Nombre d'habitants à Paris : {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille : {marseille.get_habitants()}")


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Nombre d'habitants à Paris après arrivées : {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille après arrivée : {marseille.get_habitants()}")

compte1 = CompteBancaire(12345, "Dupont", "Jean", 1000)
compte2 = CompteBancaire(67890, "Martin", "Sophie", -200, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.versement(500)
compte2.retrait(100)

compte2.agios()
compte1.virement(compte2, 200)

compte1.afficher()
compte2.afficher()
