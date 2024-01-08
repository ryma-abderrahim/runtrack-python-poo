class Rectangle:
    # Constructeur de la classe Rectangle
    def __init__(self, longueur=0, largeur=0):
        # Initialisation des attributs privés _longueur et _largeur
        self._longueur = longueur
        self._largeur = largeur

    # Méthode pour obtenir la longueur
    def getLongueur(self):
        return self._longueur

    # Méthode pour obtenir la largeur
    def getLargeur(self):
        return self._largeur
    
    # Méthode pour changer la longueur
    def setLongueur(self, new_longueur):
        self._longueur = new_longueur

    # Méthode pour changer la largeur
    def setLargeur(self, new_largeur):
        self._largeur = new_largeur

# Création d'une instance de la classe Rectangle avec une longueur de 10 et une largeur de 5
rectangle1 = Rectangle(10, 5)

# Affichage de la longueur et de la largeur initiales
print(f"Longueur : {rectangle1.getLongueur()}")
print(f"Largeur : {rectangle1.getLargeur()}")

# Modification de la longueur et de la largeur
rectangle1.setLongueur(15)
rectangle1.setLargeur(8)

# Affichage de la longueur et de la largeur après modification
print(f"Longueur après modification : {rectangle1.getLongueur()}")
print(f"Largeur après modification : {rectangle1.getLargeur()}")