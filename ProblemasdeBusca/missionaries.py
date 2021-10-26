from __future__ import annotations
from typing import List, Optional
from genericSearch import bfs, nodeToPath, Node

# Quantidade máxima de missionários
MAX_NUM = 3
class MCState:
    def __init__(self, missionaries, cannibals, boat: bool) -> None:
        self.om = missionaries # Missionários na margem oeste
        self.oc = cannibals # Cannibais na margem oeste
        self.lm = MAX_NUM - self.om # Missionários na margem leste
        self.lc = MAX_NUM - self.oc # Cannibais na margem leste
        self.boat = boat
    
    def __str__(self) -> str:
        return ("On the west bank there are {} missionaries and {} cannibals\n"
        "On the east bank there are {} missionaries and {} cannibals\n"
        "The boat is on the {} bank")\
        .format(self.om, self.oc, self.lm, self.lc, ("west" if self.boat else "east"))

    def goalTest(self) -> bool:
        return self.isLegal and self.lm == MAX_NUM and self.lc == MAX_NUM
    
    @property
    def isLegal(self) -> bool:
        if self.om < self.oc and self.om > 0:
            return False
        if self.lm < self.lc and self.lm > 0:
            return False
        return True
    

    def successors(self) -> List[MCState]:
        sucs = []
        if self.boat:
            if self.om > 1:
                sucs.append(MCState(self.om - 2, self.oc, not self.boat))
            if self.om > 0:
                sucs.append(MCState(self.om - 1, self.oc, not self.boat))
            if self.oc > 1:
                sucs.append(MCState(self.om, self.oc - 2, not self.boat))
            if self.oc > 0:
                sucs.append(MCState(self.om, self.oc - 1, not self.boat))
            if (self.oc > 0) and (self.om) > 0:
                sucs.append(MCState(self.om - 1, self.oc - 1, not self.boat))
        else:
            if self.lm > 1:
                sucs.append(MCState(self.om + 2, self.oc, not self.boat))
            if self.lm > 0:
                sucs.append(MCState(self.om + 1, self.oc, not self.boat))
            if self.lc > 1:
                sucs.append(MCState(self.om, self.oc + 2, not self.boat))
            if self.lc > 0:
                sucs.append(MCState(self.om, self.oc + 1, not self.boat))
            if (self.lc > 0) and (self.lm > 0):
                sucs.append(MCState(self.om + 1, self.oc + 1, not self.boat))
        return [x for x in sucs if x.isLegal]

def displaySolution(path):
    if len(path) == 0:
        return
    oldState = path[0]
    print(oldState)
    for currentState in path[1:]:
        if currentState.boat:
            print("{} missionaries and {} cannibals moved from the east bank to the west bank.\n".format(
                oldState.lm - currentState.lm, oldState.lc - currentState.lc))
        else:
            print("{} missionaries and {} cannibals moved from the west bank to the bank.\n".format(
                oldState.om - currentState.om, oldState.oc - currentState.oc))
        print(currentState)
        oldState = currentState

if __name__ == "__main__":
    start = MCState(MAX_NUM, MAX_NUM, True)
    solution = bfs(start, MCState.goalTest, MCState.successors)
    if solution is None:
        print("No solution find!\n")
    else:
        path = nodeToPath(solution)
        displaySolution(path)
