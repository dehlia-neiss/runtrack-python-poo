class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : x = {self.x}, y = {self.y}")

    def afficherX(self):
        print(f"Coordonnée x : {self.x}")

    def afficherY(self):
        print(f"Coordonnée y : {self.y}")

    def changerX(self, nouvelle_x):
        self.x = nouvelle_x
        print(f"La coordonnée x a été modifiée à : {self.x}")

    def changerY(self, nouvelle_y):
        self.y = nouvelle_y
        print(f"La coordonnée y a été modifiée à : {self.y}")
