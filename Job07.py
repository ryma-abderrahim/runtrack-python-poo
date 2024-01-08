class Personnage :
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #avancer à gauche
    def go_left(self):
        self.x -=1

    #avancer à droite 
    def go_right(self):
        self.x +=1

    #avnacer vers le bas 
    def go_down(self):
        self.y -=1

    #avancer vers le haut 
    def go_up(self):
        self.y +=1

    #Affichege des coordonnées de personnage 
    def position (self):
        return (self.x , self.y)
    
#instancier le personage
personnage1 = Personnage(3 , 4)
print("Position du personnage : ", personnage1.position())
    
#Déplacement à gauche 
personnage1.go_left()
print("la position  après un déplacement vers la gauche :", personnage1.position())

#Déplacemnt à droite 
personnage1.go_right()
print("La position après un déplacement vers la droite :", personnage1.position())

#Déplacement vers le bas 
personnage1.go_down()
print("La position après un déplacement vers le bas:", personnage1.position())

#Déplacement vers le haut 
personnage1.go_up()
print("La position après un déplacement vers le haut:", personnage1.position())