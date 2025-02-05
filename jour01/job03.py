class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        print("Résultat de l'addition :", self.nombre1 + self.nombre2)

# Job 2
print("Job 2")

# Instanciation de la classe
operation_instance = Operation(12, 3)

# Affichage de l'objet
print(operation_instance)

# Affichage des attributs nombre1 et nombre2
print("Valeur de nombre1 :", operation_instance.nombre1)
print("Valeur de nombre2 :", operation_instance.nombre2)

# Appel de la méthode addition
operation_instance.addition()
