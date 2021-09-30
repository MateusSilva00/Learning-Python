class supplyValve():

    def __init__(self):
        print("Constructor Supply Valve")
        self.flowCapacity = 1.1
    
    def __del__(self):
        print("Removing supply valve: address {}".format(id(self)))
    
    def fillWater(self):
        print("Flow:" + str(self.flowCapacity) + " litros/seg")

    def getFlow(self):
        return self.flowCapacity