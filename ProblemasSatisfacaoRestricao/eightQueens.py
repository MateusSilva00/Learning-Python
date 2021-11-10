from csp import Constraint, CSP
from typing import Dict, List, Optional

class queensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns = columns
    
    def satisfied(self, assignment) -> bool:
        #q1c = coluda da rainha 1, qir = linha da rainha 1
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):
                        return False
        return True

if __name__ == "__main__":
    columns = [1, 2, 3, 4, 5, 6, 7, 8]
    rows = {}

    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp = CSP(columns, rows)
    csp.addConstraint(queensConstraint(columns))
    solution = csp.backtrackingSearch()

    if solution is None:
        print("No solution found!\n")
    else:
        print(solution)