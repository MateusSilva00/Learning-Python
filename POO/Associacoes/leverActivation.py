class leverActivation(object):

    def __init__(self):
        print("Construtor Lever Activator")
        self.count1 = 0
        self.count2 = 0
    
    def __del__(self):  
        print("Removing Lever Activator: Address {}".format(id(self)))
    
    def turnOn(self, option = None):
        print("Lever activated")
        if type(option) == int:
            if option == 1:
                self.count1 += 1
            else:
                self.count2 += 1
        else:
            self.count2 += 1

    def report(self):
        print("Report of water use")
        print("")
        print("Number of discharges option 1: " + str(self.count1))
        print("Number of discharges option 2: " + str(self.count2))
