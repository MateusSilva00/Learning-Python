from powers import *

class Hulk(Person, SuperStrength):
    def __init__(self):
        Person.__init__(self)
        SuperStrength.__init__(self)
        self.relax()
    
    def getNervous(self):
        print("HULK DESTROOOOOY")
        self.setName("The Incredible Hulk")
        self.setOcupation("Professional destroyer")
        self.setHeight(3.20)
        self.setWeight(1230)
        self.setStrength(10000)

    def relax(self):
        print("Hulks smooke one")
        self.setName("Bruce Banner")
        self.setOcupation("Nuclear Physicist Scientist Gamma Ray Specialist")
        self.setHeight(1.70)
        self.setWeight(78)
        self.setStrength(7500)
    
class IronMan(Person, SuperStrength, Fly):
    def __init__(self):
        Person.__init__(self)
        SuperStrength.__init__(self)
        Fly.__init__(self)
        self.armorActivated = False
        self.setName("Tony Stark")
        self.setOcupation("Businessman, Bilionaire, Playboy and Philanthropist")
        self.setHeight(1.88)
        self.setWeight(90)
        self.setStrength(610)
        
    def activeArmor(self):
        self.armorActivated = True
        print("Jarvin says: Ready for the fight")
        self.setStrength(700)

    def deactiveArmor(self):
        print("Jarvis says: deactive")
        self.setStrength(610)
        self.setAltitude(0)
        self.armorActivated = False
    
    def setAltitude(self, altitude):
        if self.armorActivated:
            self.altitude = altitude
        else:
            print("Jarvis says: Can't fly without the armor")
    
    def getData(self):
        print("")
        if self.armorActivated:
            print("Armor activated: Iron Man mode")
        Person.getData(self)
        SuperStrength.getData(self)
        Fly.getData(self)
        print("")