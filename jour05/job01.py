class Part:
    def __init__(self, name: str, material: str):
     
        self.name = name
        self.material = material

    def change_material(self, new_material: str):

        self.material = new_material

    def __str__(self):
      
        return f"Pièce: {self.name}, Matériau: {self.material}"


if __name__ == "__main__":
    part = Part("Mât", "Bois")
    print(part)
    part.change_material("Acier")
    print(part)
