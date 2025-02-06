class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        return f"{self.nom} (#{self.numero}, {self.position}) - Buts: {self.buts}, Passes: {self.passes_decisives}, Jaunes: {self.cartons_jaunes}, Rouges: {self.cartons_rouges}"

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        return [joueur.afficher_statistiques() for joueur in self.joueurs]

    def mettre_a_jour_statistiques_joueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquer_un_but()
                elif action == "passe":
                    joueur.effectuer_une_passe_decisive()
                elif action == "jaune":
                    joueur.recevoir_un_carton_jaune()
                elif action == "rouge":
                    joueur.recevoir_un_carton_rouge()

equipe1 = Equipe("Paris FC")
equipe2 = Equipe("Marseille FC")

joueur1 = Joueur("Mbappé", 7, "Attaquant")
joueur2 = Joueur("Neymar", 10, "Milieu")
joueur3 = Joueur("Ramos", 4, "Défenseur")

joueur4 = Joueur("Payet", 10, "Milieu")
joueur5 = Joueur("Benedetto", 9, "Attaquant")

equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)
equipe1.ajouter_joueur(joueur3)

equipe2.ajouter_joueur(joueur4)
equipe2.ajouter_joueur(joueur5)

equipe1.mettre_a_jour_statistiques_joueur("Mbappé", "but")
equipe1.mettre_a_jour_statistiques_joueur("Neymar", "passe")
equipe2.mettre_a_jour_statistiques_joueur("Payet", "jaune")
equipe2.mettre_a_jour_statistiques_joueur("Benedetto", "rouge")

print("Statistiques de l'équipe Paris FC:")
print(equipe1.afficher_statistiques_joueurs())
print("\nStatistiques de l'équipe Marseille FC:")
print(equipe2.afficher_statistiques_joueurs())
