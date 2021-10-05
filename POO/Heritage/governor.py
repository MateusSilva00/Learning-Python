from political import Political

class Governor(Political):

    def __init__(self, name, party, state):
        Political.__init__(self)
        self.setName(name)
        self.setParty(party)
        self.setState(state)
        self.setFunction("Manage things aswell as I know")

    def introduction(self):
        Political.introduction(self)
        print("I am Governor")
        print("My function is + " + self.getFunction)
        print("I was elected by " + self.getState)
        print("==================================")
