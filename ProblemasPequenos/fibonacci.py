from typing import Dict, Generator
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}

def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)

def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]

# Sempre que fib3 fora executado com um novo argumento, o decorador fará com que o valor de retorno
# seja armazenado em cache
@lru_cache(maxsize = None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n - 2) + fib3(n - 1)

# Forma mais eficiente
def fib4(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def fib5(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next # Passo para geração do próximo valor

if __name__ == "__main__":
    print(fib1(10))
    print(fib2(20))
    print(fib3(30))
    print(fib4(32))
    
    for i in fib5(10):
        print(i, end = " ")

