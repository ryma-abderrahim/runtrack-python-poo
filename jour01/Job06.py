class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def afficherAge(self):
        return f"L'âge de l'animal est  {self.age} ans "

    def vieillir(self):
        self.age += 1

    def nommer(self,nom):
        self.prenom=nom

    def afficherNom(self):
        return f"l'animal se nomme {self.prenom}"

# Instancier un animal
animal1 = Animal(5, "Mimi")

# Imprimer l'âge de l'animal en console
print(animal1.afficherAge())

# Faire vieillir l'animal
animal1.vieillir()

# Imprimer l'âge de l'animal en console après vieillissement
print(animal1.afficherAge())

#Imprimer le nom de l'animal en console 
print(animal1.afficherNom())

# Changer le nom de l'animal
animal1.nommer("Coco")

#Imprimer le nouveau nom de l'animal
print(animal1.afficherNom())