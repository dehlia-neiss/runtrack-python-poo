class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_instance = Operation(12, 3)

print(operation_instance)

print("Valeur de nombre1 :", operation_instance.nombre1)
print("Valeur de nombre2 :", operation_instance.nombre2)
