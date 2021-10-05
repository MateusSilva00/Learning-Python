from president import President
from senator import Senator
from congressman import Congressman
from governor import Governor
from stateDeputy import StateDeputy
from mayor import Mayor
from councilor import Councilor

PRES = President("Jair Messias Bolsonaro", "Social Liberal")
DEPF = Congressman("Jean Willis", "Socialist", "RJ")
SEN = Senator("Júlio Cesar", "Greek", "ÁGORA")
DEPE = StateDeputy("Mommy I Spoke", "Democrat", "SP")

PRES.introduction()
DEPF.introduction()
SEN.introduction()
DEPE.introduction()