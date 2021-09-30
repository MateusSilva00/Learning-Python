from secrets import token_bytes
from typing import Tuple

def randomKey(lengh: int) -> int:
    tb: bytes = token_bytes(lengh)
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    if original is not str:
        original = str(original)
    originalBytes: bytes = original.encode()
    dummy: int = randomKey(len(originalBytes))    
    originalKey: int = int.from_bytes(originalBytes, "big")
    encrypted: int = originalKey ^ dummy
    return dummy, encrypted

if __name__ == "__main__":

    imageName = "goku.jpg"
    fin = open(imageName, 'rb')

    image = fin.read()
    fin.close()

    key1, key2 = encrypt(image)

    fin = open(imageName, 'wb')
    fin.close()
    print("Encryption Done...")
