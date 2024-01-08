class Commande:
    def __init__(self, numero_commande, statut):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut = statut

    def ajouter_plat(self, nom, prix):
        self.__plats_commandes[nom] = {'prix': prix, 'statut': 'en cours'}

    def annuler_commande(self):
        self.__statut = 'annulée'

    def __calculer_total(self):
        total = sum(plat['prix'] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        total = self.__calculer_total()
        print("Commande n°{}".format(self.__numero_commande))
        print("\tStatut : {}".format(self.__statut))
        print("plats:")
        for plat, details in self.__plats_commandes.items():
            print(f"       {plat}   {details['prix']}  {details['statut']}")
        print(f"Total à payer : {total}")

    def calculer_TVA(self, taux_TVA):
        total = self.__calculer_total()
        tva = total * (taux_TVA / 100)
        return tva
    
# Création d'une commande
ma_commande = Commande("001", "en cours")

# Ajout d'un plat à la commande
ma_commande.ajouter_plat("Pizza", 12.50)
ma_commande.ajouter_plat("Salade",10.90)
ma_commande.ajouter_plat("glace", 4.50)

# Affichage de la commande
ma_commande.afficher_commande()

# Calcul de la TVA pour la commande
tva = ma_commande.calculer_TVA(20)
print(f"TVA à payer : {tva}")

print("\n annuler la conmmande \n")
# Annulation de la commande
ma_commande.annuler_commande()

# Affichage de la commande aprés l'annulation
ma_commande.afficher_commande()
