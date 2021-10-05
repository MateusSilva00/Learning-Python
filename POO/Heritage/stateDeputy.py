from political import Political

class StateDeputy(Political):

    def __init__(self, name, party, state):
        Political.__init__(self)
        self.setName(name)
        self.setParty(party)
        self.setState(state)
        self.setFunction("Proporse state laws to be broken")
    
    def introduction(self):
        super(StateDeputy, self).introduction()
        print("I am State Deputy")
        print("My function is " + self.getFunction())
        print("I was elected by " + self.getState())
        print("==================================")