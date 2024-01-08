class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return f"Les coordonnées du point sont : ({self.x}, {self.y})"

    def afficherX(self):
        return f"La coordonnée x du point est : {self.x}"

    def afficherY(self):
        return f"La coordonnée y du point est : {self.y}"

    def changerX(self, nouveau_x):
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y

# Instancier un point
point1 = Point(5, 7)

# Imprimer les coordonnées du point en console
print(point1.afficherLesPoints())

# Imprimer la coordonnée x du point en console
print(point1.afficherX())

# Imprimer la coordonnée y du point en console
print(point1.afficherY())

# Changer la valeur de l'attribut x
point1.changerX(10)

# Changer la valeur de l'attribut y
point1.changerY(15)

# Imprimer les coordonnées du point en console après modification
print(point1.afficherLesPoints())