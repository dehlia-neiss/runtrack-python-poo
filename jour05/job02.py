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

    def add_part(self, part: Part):
        self.__parts[part.name] = part

    def display_state(self):
        print(f"État du bateau {self.name}:")
        for part in self.__parts.values():
            print(part)

    def replace_part(self, part_name: str, new_part: Part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
        else:
            print(f"La pièce {part_name} n'existe pas dans le bateau.")

if __name__ == "__main__":
    part1 = Part("Mât", "Bois")
    part2 = Part("Coque", "Acier")
    ship = Ship("Titanic")
    ship.add_part(part1)
    ship.add_part(part2)
    ship.display_state()
    new_part = Part("Mât", "Acier")
    ship.replace_part("Mât", new_part)
    ship.display_state()
