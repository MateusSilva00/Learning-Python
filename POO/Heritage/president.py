from political import Political

class President(Political):

    def __init__(self, name, party):
        Political.__init__(self)
        self.setName(name)
        self.setParty(party)
        self.setState("")
        self.setFunction("Good administration of federal taxes on behalf of the people ")
    
    def introduction(self):
        super(President, self).introduction()
        print("I am the Dictorship")
        print("My function is " + self.getFunction())
        print("I was elected by " + self.getState())
        print("=================================")
