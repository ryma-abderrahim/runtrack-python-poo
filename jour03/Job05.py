import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        adversaire.subir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts!")

    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancer_jeu(self):
        joueur = Personnage("Joueur", self.niveau * 10)
        ennemi = Personnage("Ennemi", self.niveau * 5)

        while joueur.vie > 0 and ennemi.vie > 0:
            print(f"\nTour suivant - Niveau {self.niveau}")
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

            print(f"\n{ joueur.nom }: Vie = { joueur.vie } points")
            print(f"{ ennemi.nom }: Vie = { ennemi.vie } points")

        if joueur.vie > 0:
            print(f"\nBravo! { joueur.nom } a vaincu l'ennemi!")
        else:
            print(f"\nDommage! { ennemi.nom } a vaincu { joueur.nom }.")

# Exemple d'utilisation
jeu = Jeu()
jeu.choisir_niveau()
jeu.lancer_jeu()
