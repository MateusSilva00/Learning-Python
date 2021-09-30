from secrets import token_bytes
from typing import Tuple

def randomKey(lengh: int) -> int:
    tb: bytes = token_bytes(lengh);
    # Convertendo bytes em uma cadeia de bits
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    originalBytes: bytes = original.encode()
    dummy: int = randomKey(len(originalBytes))
    originalKey: int = int.from_bytes(originalBytes, "big")
    encrypted: int = originalKey ^ dummy # ^ = operador XOR (ou exclusivo)
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("One time pad!");
    print(key1, key2)
    result: str = decrypt(key1, key2)
    print(result)
