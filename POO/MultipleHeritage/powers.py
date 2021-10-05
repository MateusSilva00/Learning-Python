class SuperStrength:
    def __init__(self):
        print("I have a super strength!")
        self.power = 0

    def getStrength(self):
            return self.power
        
    def setStrength(self, power):
        self.power = power
    
    def getData(self):
        print("Strength: " + str(self.getStrength()))

class Fly:
    def __init__(self):
        print("I can fly!")
        self.altitude = 0
    
    def getAltitude(self):
        return self.altitude
    
    def setAltitude(self, altitude):
        self.altitude = altitude
    
    def getData(self):
        if self.getAltitude() > 0: 
            print("Fly in " + str(self.getAltitude()) + " meters")


class Person:
    def __init__(self):
        print("I am person")
        self.name = "NOT REVEALED"
        self.ocupation = "NOT REVEALED"
        self.sex = "Male"
        self.weight = 0
        self.height = 0
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getOcupation(self):
        return self.ocupation
    
    def setOcupation(self, ocupation):
        self.ocupation = ocupation
    
    def getSex(self):
        return self.sex
    
    def setSex(self, sex):
        self.sex = sex

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight
    
    def getHeight(self):
        return self.height
    
    def setHeight(self, height):
        self.height = height

    def getData(self):
        print("Name: " + self.getName())
        print("Sex: " + self.getName())
        print("Function: " + self.getOcupation())
        print("Weight: " + str(self.getWeight()))
        print("Height: " + str(self.getHeight()))
