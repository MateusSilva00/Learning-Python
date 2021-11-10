from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')
D = TypeVar('D')

class Constraint(Generic[V, D], ABC):
    def __init__(self, variables) -> None:
        self.variables = variables


    @abstractmethod
    def satisfied(self, assignment) -> bool:
        ...

class CSP(Generic[V, D]):
    def __init__(self, variables, domains: Dict[V, List[D]]) -> None:
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it")
    
    def addConstraint(self, constraint) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)
    
    def consistent(self, variable, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    

    def backtrackingSearch(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.variables):
            return assignment
        
        # Obtém todas as variáveis que estão em CSP mas não é assignment
        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]

        for value in self.domains[first]:
            localAssignment = assignment.copy()
            localAssignment[first] = value
            if self.consistent(first, localAssignment):
                result = self.backtrackingSearch(localAssignment)
                if result is not None:
                    return result
        return None
