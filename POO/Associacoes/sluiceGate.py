class sluiceGate(object):
    def __init__(self):
        print("Construtor Sluice Gate")
        self.status = "Closed"
    
    def __del__(self):
        print("Removing sluice gate: address {}".format(id(self)))

    def open(self, flowRate = None):
        if flowRate == None:
            print("Sluice gate is open. All water coming out")
        else:
            print("Sluice is open. Out "+ str(flowRate) + " water")
        
        self.status = "Opened"
    
    def close(self):
        print("Sluice gate is closed")
        self.status = "Closed"
    
    def getStatus(self):
        return self.status