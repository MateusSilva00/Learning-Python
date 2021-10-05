class Political:

    def __init__(self):
        self.__name = ""
        self.__party = ""
        self.__state = ""
        self.__function = ""
    
    def setName(self, name):
        if type(name) == str:
            self.__name = name
    
    def getName(self):
        return self.__name
    
    def setParty(self, party):
        if type(party) == str:
            self.__party = party
    
    def getParty(self):
        return self.__party
    
    def setState(self, state):
        if type(state) == str:
            self.__state = state
    
    def getState(self):
        return self.__state

    def setFunction(self, function):
        if type(function) == str:
            self.__function = function
    
    def getFunction(self):
        return self.__function
    
    def introduction(self):
        print("Hi, I'm  " + self.getName())
        print("From the " + self.getParty() + " party")