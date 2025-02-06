import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    
    def get_valeur(self):
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10
        elif self.valeur == "As":
            return 11  # La gestion de l'As sera ajustée plus tard
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)
    
    def tirer_carte(self):
        return self.paquet.pop()

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.joueur_main = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]
        self.croupier_main = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]
    
    def calculer_score(self, main):
        score = sum(carte.get_valeur() for carte in main)
        nombre_as = sum(1 for carte in main if carte.valeur == "As")
        while score > 21 and nombre_as:
            score -= 10
            nombre_as -= 1
        return score
    
    def afficher_main(self, main):
        return ", ".join(str(carte) for carte in main)
    
    def jouer(self):
        print("Votre main :", self.afficher_main(self.joueur_main))
        while self.calculer_score(self.joueur_main) < 21:
            action = input("Voulez-vous tirer une carte ? (o/n) : ")
            if action.lower() == "o":
                self.joueur_main.append(self.jeu.tirer_carte())
                print("Votre main :", self.afficher_main(self.joueur_main))
            else:
                break
        
        if self.calculer_score(self.joueur_main) > 21:
            print("Vous avez dépassé 21, vous perdez !")
            return
        
        print("Main du croupier :", self.afficher_main(self.croupier_main))
        while self.calculer_score(self.croupier_main) < 17:
            self.croupier_main.append(self.jeu.tirer_carte())
            print("Main du croupier :", self.afficher_main(self.croupier_main))
        
        score_joueur = self.calculer_score(self.joueur_main)
        score_croupier = self.calculer_score(self.croupier_main)
        
        print(f"Votre score : {score_joueur}, Score du croupier : {score_croupier}")
        if score_croupier > 21 or score_joueur > score_croupier:
            print("Félicitations, vous avez gagné !")
        elif score_joueur < score_croupier:
            print("Désolé, le croupier gagne !")
        else:
            print("Égalité !")

partie = Blackjack()
partie.jouer()