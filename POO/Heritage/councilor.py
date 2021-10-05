from political import Political

class Councilor(Political):

    def __init__(self, name, party, city, state):
        Political.__init__(self)
        self.setName(name)
        self.setParty(party)
        self.setState(state)
        self.__city = city

    def setCity(self, city):
        if type(city) == str:
            self.__city = city
    
    def getCity(self):
        return self.__city
    
    def introduction(self, city):
        Political.introduction(self)
        print("I am Councilor of " + self.getCity())
        print("My function is " + self.getFunction())
        print("I was elected by " + self.getState())
        print("==================================")
