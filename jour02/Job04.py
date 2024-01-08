class Student :
    def __init__(self, name="" , surname="" , numbre=0 , credits=0 , level=""):
        self._name = name
        self._surname = surname
        self._numbre = numbre
        self._credits= credits
        self._level = level
  

    #getter and setter of name 
    def getName(self):
        return self._name
    
    def setName ( self, new_name):
        self._name = new_name

    
    #getter and setter of the surname 
    def getSurname(self):
        return self._surname
    
    def setSurname ( self, new_surname):
        self._surname = new_surname

    
    #getter and setter of the student numbre
    def getNumber ( self):
        return self._numbre
    
    def setNumber ( self, new_number):
        self._numbre =new_number

    
    #getter and setter of the credits number
    def getCredits(self):
        return self._credits
    
    def setCredits(self, new_credits):
        if new_credits>=0 :
            self._credits= new_credits

 
   #getter of the student level
    def getLevel(self):
        return self._level


    def add_credits (self , new_credit):
        credits=(self.getCredits()) + new_credit
        self.setCredits(credits)

    #StudentEval Methode
    def studentEval(self):
        if self._credits>= 90 :
            self._level = "Exceellent"
        elif self._credits>=80:
            self._level = "Trés Bien"
        elif self._credits >=70:
            self._level = "Bien"
        elif self._credits >=60:
            self._level = "Passable"
        else:
            self._level = "Insuffisant"
        

    def studentInfo(self):
        print("Nom:", self._name)
        print("Prénom:", self._surname)
        print("Identifiant:", self._numbre)
        print("Niveau:", self._level)


#intance of the student class
S1=Student("John", "Doe" , 145,10 ,"")

print(f"le nombre de credits de {S1.getName()} est de {S1.getCredits()} points")

#add 15 points to the credits number of John Doe
S1.add_credits(15)
print(f"le nombre de credits de {S1.getName()} est de {S1.getCredits()} points")

#add 5 ponits to the credits number of John Doe
S1.add_credits(5)
print(f"le nombre de credits de {S1.getName()} est de {S1.getCredits()} points")

S1.studentEval()
S1.studentInfo()