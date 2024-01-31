class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def getNom(self):
        return self.__nom

    def getPopulation(self):
        return self.__population

    def ajouterPopulation(self, valeur):
        self.__population += valeur


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.ajouterPopulation(1)


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Paris: {paris.getPopulation()} habitants")
print(f"Population de la vlle de Marseille: {marseille.getPopulation()} habitants")

john = Personne("John", 45, paris)
john.ajouterPopulation()

myrtille = Personne("Myrtille", 4, paris)
myrtille.ajouterPopulation()

chloe = Personne("Chloé", 18, marseille)
chloe.ajouterPopulation()

print(f"Mise à jour de la population de la ville de Paris: {paris.getPopulation()} habitants")
print(f"Mise à jour de la population de la ville de Marseille: {marseille.getPopulation()} habitants")
