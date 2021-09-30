""" COUPLED BOX"""
from leverActivation import leverActivation
from supplyValve import supplyValve
from sluiceGate import sluiceGate

class coupledBox(object):

    # Método construtor
    def __init__(self):
        print("Toilet Box Construtor")
        self.lever = leverActivation()
        self.valve = supplyValve()
        self.sluice = sluiceGate()
        self.maxLevel = 6.0
        self.waterLevel = 0.0
        self.fillBox()

    # Método destrutor
    def __del__(self):
        print("Removing toiled box: address {}".format(id(self)))


    def fillBox(self):
        print("Fill the coupled Box")
        while self.waterLevel < self.maxLevel:
            self.waterLevel = self.waterLevel + self.valve.getFlow()
            if self.waterLevel > self.maxLevel:
                self.waterLevel = self.maxLevel
            print("Water level: " + str(round(self.waterLevel, 2))) 
    
    def turnOn(self, option=None):
        print("Turned on the toilet box")

        if type(option) == int:
            if option == 1:
                print("Number 1: Not much water")
                self.lever.turnOn(option)
                self.sluice.open()
                self.waterLevel = self.maxLevel / 2
                self.sluice.close()
                self.valve.fillWater()
                self.fillBox()
            elif option == 2:
                print("Number 2: More water")
                self.lever.turnOn(option)
                self.sluice.open()
                self.waterLevel = 0
                self.sluice.close()
                self.valve.fillWater()
                self.fillBox()        
            else:
                print("Unknow option!")

        else:
            print("That's not a smart toilet...")
            self.lever.turnOn()
            self.sluice.open()
            self.waterLevel = 0
            self.sluice.close()
            self.valve.fillWater()
            self.fillBox()
    
    def report(self):
        self.lever.report()
