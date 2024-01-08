class Personne:
    def __init__(self, nom=None, prenom=None):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je suis {self.nom} {self.prenom}"

# Instancier la première personne
personne1 = Personne("John", "Doe")

# Imprimer les attributs "nom" et "prenom" en console
print(personne1.se_presenter())

# Instancier la deuxième personne
personne2 = Personne("Jean", "Dupond")

# Imprimer les attributs "nom" et "prenom" en console
print(personne2.se_presenter())
 