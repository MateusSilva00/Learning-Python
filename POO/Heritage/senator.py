from political import Political

class Senator(Political):

    def __init__(self, name, party, state):
        Political.__init__(self)
        self.setName(name)
        self.setParty(party)
        self.setState(state)
        self.setFunction("Propose laws to be broken")
    
    def introduction(self):
        Political.introduction(self)
        print("I am senator")
        print("My function is " + self.getFunction())
        print("I was elected by " + self.getState())
    