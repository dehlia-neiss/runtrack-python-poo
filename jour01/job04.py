class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        print("Résultat de l'addition :", self.nombre1 + self.nombre2)

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."

print("Job 2")

operation_instance = Operation(12, 3)
print(operation_instance)
print("Valeur de nombre1 :", operation_instance.nombre1)
print("Valeur de nombre2 :", operation_instance.nombre2)
operation_instance.addition()

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupont")


print(personne1.SePresenter())
print(personne2.SePresenter())

