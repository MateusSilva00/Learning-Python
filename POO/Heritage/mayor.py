from political import Political

class Mayor(Political):
    
    def __init__(self, name, party, city, state):
        Political.__init__(self)
        self.setName(name)
        self.setParty(party)
        self.setState(state)
        self.__city = city
        self.setFunction("Manage the city")
    
    def setCity(self, city):
        if type(city) == str:
            self.__city = city
    
    def getCity(self):
        return self.__city

    def introduction(self):
        Political.introduction(self)
        print("I am mayor of + " + self.getCity())
        print("My function is " + self.getFunction())
        print("I was elected by " + self.getState())
        print("==================================")
