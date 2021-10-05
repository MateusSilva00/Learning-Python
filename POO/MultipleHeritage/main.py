from heroes import *

if __name__ == "__main__":
    MarkRuffalo = Hulk()
    MarkRuffalo.getData()
    MarkRuffalo.getNervous()
    MarkRuffalo.getData()
    MarkRuffalo.relax()
    MarkRuffalo.getData()
    
    print("===================================")
    RobertDowney = IronMan()
    RobertDowney.getData()
    RobertDowney.setAltitude(150)
    RobertDowney.activeArmor()
    RobertDowney.setAltitude(150)
    RobertDowney.getData()
    RobertDowney.deactiveArmor()
    RobertDowney.getData()