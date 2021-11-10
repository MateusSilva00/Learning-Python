from csp import Constraint, CSP
from typing import Dict, List, Optional

class mapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1, place2) -> None:
        super().__init__([place1, place2])
        self.place1 = place1
        self.place2 = place2

    def satisfied(self, assignment) -> bool:
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        
        return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
    variables = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales", "Victoria", "Tasmania"]
    domains: Dict[str, List[str]] = {}
    
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]
    csp = CSP(variables, domains)
    csp.addConstraint(mapColoringConstraint("Western Australia", "Northern Territory"))
    csp.addConstraint(mapColoringConstraint("Western Australia", "South Australia"))
    csp.addConstraint(mapColoringConstraint("South Australia", "Northern Territory"))
    csp.addConstraint(mapColoringConstraint("Queensland", "Northern Territory"))
    csp.addConstraint(mapColoringConstraint("Queensland", "South Australia"))
    csp.addConstraint(mapColoringConstraint("Queensland", "New South Wales"))
    csp.addConstraint(mapColoringConstraint("New South Wales", "South Australia"))
    csp.addConstraint(mapColoringConstraint("Victoria", "South Australia"))
    csp.addConstraint(mapColoringConstraint("Victoria", "New South Wales"))
    csp.addConstraint(mapColoringConstraint("Victoria", "Tasmania"))

    solution = csp.backtrackingSearch()
    if solution is None:
        print("No solution found!\n")
    else:
        print(solution)
