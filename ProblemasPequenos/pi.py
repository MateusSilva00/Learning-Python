def calcPi(nTerms: int) -> float:
    numerador: float = 4.0
    demoninador: float = 1.0
    operacao: float = 1.0
    pi: float = 0.0

    # Leibniz definition
    for _ in range(nTerms):
        pi += operacao * (numerador / demoninador)
        demoninador += 2.0
        operacao *= -1
    return pi

if __name__ == "__main__":
    print(calcPi(99999))