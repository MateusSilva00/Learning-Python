from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linearSearch(iterable, key) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other) -> bool:
        ...
    
    def __lt__(self: C, other: C) -> bool:
        ...
    
    def __gt__(self: C, other: C) -> bool:
        return(not self < other) and self != other

    def __ge__(self: C, other: C) -> bool:
        return not self < other 

def binarySearch(sequence, key) -> bool:
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False

class Stack(Generic[T]):
    def __init__(self):
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container 

    def push(self, item) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop() 

    def __repr__(self) -> str:
        return repr(self._container)

class Node(Generic[T]):
    def __init__(self, state, parent: Optional[Node], cost:float = 0.0, heuristic: float = 0.0) -> None:
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initial, goalTest: Callable[[T], bool], successors:Callable[[T], List[T]]) -> Optional[Node[T]]:
  
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))

    explored: Set[T] = {initial}


    while not frontier.empty:
        currentNode: Node[T] = frontier.pop()
        currentState: T = currentNode.state

        if goalTest(currentState):
            return currentNode
        for child in successors(currentState):
            if child in explored: 
                continue
            explored.add(child)
            frontier.push(Node(child, currentNode))
    return None  


def nodeToPath(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
   
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


class Queue(Generic[T]):
    def __init__(self):
        self._container: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        return not self._container  

    def push(self, item) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()  

    def __repr__(self) -> str:
        return repr(self._container)


def bfs(initial, goalTest: Callable[[T], bool], successors:Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    explored: Set[T] = {initial}
    
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
       
        if goalTest(current_state):
            return current_node
   
        for child in successors(current_state):
            if child in explored:  
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None  


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  

    def push(self, item: T) -> None:
        heappush(self._container, item)  

    def pop(self) -> T:
        return heappop(self._container)  

    def __repr__(self) -> str:
        return repr(self._container)


def astar(initial, goalTest, sucessors: Callable[[T], List[T]], heuristic) -> Optional[Node[T]]:
    # Lugares que devemos visitar
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}

    while not frontier.empty:
        currentNode = frontier.pop()
        currentState = currentNode.state
        if goalTest(currentState):
            return currentNode # Se encontrar o caminho
        for child in sucessors(currentState):
            newCost = currentNode.cost + 1
            if child not in explored or explored[child] > newCost:
                explored[child] = newCost
                frontier.push(Node(child, currentNode, newCost, heuristic(child)))
    return None # Passou por todos lugares e não encontrou o objetivo

if __name__ == "__main__":
    print(linearSearch([1,5,15,15,15,15,20], 5))
    print(binarySearch(["a", "d", "e", "f", "z"], "f"))
    print(binarySearch(["john", "marcos", "ronaldo", "sarah"], "sheilason"))
