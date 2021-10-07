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

if __name__ == "__main__":
    print(linearSearch([1,5,15,15,15,15,20], 5))
    print(binarySearch(["a", "d", "e", "f", "z"], "f"))
    print(binarySearch(["john", "marcos", "ronaldo", "sarah"], "sheilason"))