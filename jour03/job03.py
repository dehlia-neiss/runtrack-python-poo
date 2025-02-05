class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquer_comme_finie(self):
        self.statut = "Terminée"

    def __str__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def marquer_comme_finie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquer_comme_finie()

    def afficher_liste(self):
        return [str(tache) for tache in self.taches]

    def filter_liste(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]

todo_list = ListeDeTaches()
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Finir le projet", "Terminer la partie backend")
tache3 = Tache("Réviser l'examen", "Relire les chapitres 3 et 4")

todo_list.ajouter_tache(tache1)
todo_list.ajouter_tache(tache2)
todo_list.ajouter_tache(tache3)

todo_list.marquer_comme_finie("Faire les courses")
todo_list.supprimer_tache("Finir le projet")

print("Toutes les tâches:", todo_list.afficher_liste())
print("Tâches à faire:", todo_list.filter_liste("À faire"))
