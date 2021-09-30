from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)


numDisc: int = 3;
towerA: Stack[int] = Stack()
towerB: Stack[int] = Stack()
towerC: Stack[int] = Stack()

for i in range (1, numDisc + 1):
    towerA.push(i)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n -1)

if __name__ == "__main__":
    hanoi(towerA, towerC, towerB, numDisc)
    print(towerA)
    print(towerB)
    print(towerC)
