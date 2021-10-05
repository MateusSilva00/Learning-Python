from political import Political

class Congressman(Political):

    def __init__(self, name, party, state):
        Political.__init__(self)
        self.setName(name)
        self.setParty(party)
        self.setState(state)
        self.setFunction("Propose federal laws to be broken")

    def introduction(self):
        super(Congressman, self).introduction()
        print("I am Congressman")
        print("My function is " + self.getFunction())
        print("I was elected by " + self.getState())
        print("=================================")
