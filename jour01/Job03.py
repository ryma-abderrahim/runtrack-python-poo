class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Le nombre1 est {self.nombre1} \nLe nombre2 est {self.nombre2}"

    def addition(self):
        result= self.nombre1 + self.nombre2
        print(f"le resultat de l'addition est : {result}")
# Instancier la première classe
op1 = Operation(5, 3)

# Imprimer les attributs "nombre1" et "nombre2" en console
print(op1)

#utiliser la méthode addition() pour calculer la somme des deux nombre 
op1.addition()