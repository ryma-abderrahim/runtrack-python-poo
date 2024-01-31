class Joueur :
    def __init__(self,nom, num, position, nbBut=0, passDecisif=0, cartonJaune=0, cartonRouge=0):
        self._nom = nom
        self._numero = num
        self._position = position
        self._nbButs = nbBut
        self._passesDecisifs = passDecisif
        self._cartonsJaunes = cartonJaune
        self._cartonsRouges = cartonRouge

    def marquerUnBut(self):
        self._nbButs += 1

    def effectuerUnePasseDecisive(self):
        self._passesDecisifs += 1

    def recevoirUnCartinJaune(self):
        self._cartonsJaunes += 1

    def recevoirUnCartinRouge(self):
        self._cartonsRouges += 1

    def afficherStatistiques(self):
        print("Nom: ", self._nom)
        print("Numéro: ", self._numero)
        print("Position: ", self._position)
        print("Nombre de buts: ", self._nbButs)
        print("Passes décisives: ", self._passesDecisifs)
        print("Nombre de carton jaune: ", self._cartonsJaunes)
        print("Nombre de carton rouge: ", self._cartonsRouges)



######################"" Class Equipe ""##########################
class Equipe : 

    def __init__ (self , nom):
        self._joueurs = []
        self._nom = nom
        
    
    def ajouterJoueur(self, joueur):
            self._joueurs.append(joueur)
       
    
    def AfficherStatistiqueJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self._nom}:")
        for joueur in self._joueurs:
            joueur.afficherStatistiques()
            print("\n")


    def mettreAJourStatistiquesJoueur(self, nom, buts=0, passes_décisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self._joueurs:
            if joueur._nom == nom:
                joueur._nbButs += buts
                joueur._passesDecisifs += passes_décisives
                joueur._cartonsJaunes += cartons_jaunes
                joueur._cartonsRouges += cartons_rouges
                return
        print(f"Aucun joueur nommé '{nom}' trouvé dans l'équipe {self._nom}.")
            

#creation des joueurs 
joueur1=Joueur("John Doe", 10 , "Attaquant")
joueur2=Joueur("Brayan Dally" , 5 , "Défenseur")
joueur3=Joueur("Toto Fen" , 7 , "Attaquant")

#création de l'équipe 
equipe=Equipe("Team 1")
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

#afficher les statistique de la Team A
equipe.AfficherStatistiqueJoueurs()

#simuler le match
joueur1.marquerUnBut()
joueur2.afficherStatistiques()
joueur3.recevoirUnCartinJaune()
joueur1.recevoirUnCartinRouge()

equipe.AfficherStatistiqueJoueurs()

equipe.mettreAJourStatistiquesJoueur("John Doe" , 1 ,0,0,1)
equipe.AfficherStatistiqueJoueurs()
