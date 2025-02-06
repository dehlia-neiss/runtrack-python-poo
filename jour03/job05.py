import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts!")

    def est_vivant(self):
        return self.vie > 0

    def afficher_vie(self):
        print(f"{self.nom} a {self.vie} points de vie restants.")

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisir_niveau(self):
        niveaux = {"facile": 100, "moyen": 75, "difficile": 50}
        while self.niveau not in niveaux:
            self.niveau = input("Choisissez un niveau (facile, moyen, difficile) : ").lower()
        points_de_vie = niveaux[self.niveau]
        self.joueur = Personnage("Héros", points_de_vie)
        self.ennemi = Personnage("Monstre", points_de_vie)

    def lancer_jeu(self):
        self.choisir_niveau()
        print("Début du combat !")
        while self.joueur.est_vivant() and self.ennemi.est_vivant():
            self.joueur.attaquer(self.ennemi)
            if self.ennemi.est_vivant():
                self.ennemi.attaquer(self.joueur)
            self.joueur.afficher_vie()
            self.ennemi.afficher_vie()
        self.verifier_victoire()

    def verifier_victoire(self):
        if self.joueur.est_vivant():
            print("Félicitations ! Vous avez gagné !")
        else:
            print("Dommage... Vous avez perdu.")

jeu = Jeu()
jeu.lancer_jeu()
