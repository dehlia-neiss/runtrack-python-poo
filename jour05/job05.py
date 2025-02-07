class Part:
    def __init__(self, name: str, material: str):
        self.name = name
        self.material = material

    def change_material(self, new_material: str):
        self.material = new_material

    def __str__(self):
        return f"Pièce: {self.name}, Matériau: {self.material}"

class Ship:
    def __init__(self, name: str):
        self.name = name
        self.__parts = {}
        self.history = []

    def add_part(self, part: Part):
        self.__parts[part.name] = part
        self.history.append(f"Ajout de la pièce: {part}")

    def display_state(self):
        print(f"État du bateau {self.name}:")
        for part in self.__parts.values():
            print(part)

    def replace_part(self, part_name: str, new_part: Part):
        if part_name in self.__parts:
            self.history.append(f"Remplacement de {self.__parts[part_name]} par {new_part}")
            self.__parts[part_name] = new_part
        else:
            print(f"La pièce {part_name} n'existe pas dans le bateau.")

    def change_part(self, part_name: str, new_material: str):
        if part_name in self.__parts:
            old_material = self.__parts[part_name].material
            self.__parts[part_name].change_material(new_material)
            self.history.append(f"Modification de {part_name}: {old_material} -> {new_material}")
        else:
            print(f"La pièce {part_name} n'existe pas dans le bateau.")

    def display_history(self):
        print("Historique des modifications:")
        for entry in self.history:
            print(entry)

class RacingShip(Ship):
    def __init__(self, name: str, max_speed: float):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse maximale du {self.name}: {self.max_speed} nœuds")

if __name__ == "__main__":
    ship = Ship("Titanic")
    while True:
        print("\nMenu interactif:")
        print("1. Ajouter une pièce")
        print("2. Modifier le matériau d'une pièce")
        print("3. Remplacer une pièce")
        print("4. Afficher l'état du bateau")
        print("5. Afficher l'historique")
        print("6. Quitter")
        choix = input("Choisissez une option: ")
        
        if choix == "1":
            name = input("Nom de la pièce: ")
            material = input("Matériau: ")
            ship.add_part(Part(name, material))
        elif choix == "2":
            name = input("Nom de la pièce à modifier: ")
            material = input("Nouveau matériau: ")
            ship.change_part(name, material)
        elif choix == "3":
            name = input("Nom de la pièce à remplacer: ")
            material = input("Matériau de la nouvelle pièce: ")
            ship.replace_part(name, Part(name, material))
        elif choix == "4":
            ship.display_state()
        elif choix == "5":
            ship.display_history()
        elif choix == "6":
            break
        else:
            print("Option invalide, veuillez réessayer.")
