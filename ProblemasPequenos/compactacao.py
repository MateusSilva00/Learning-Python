from sys import getsizeof
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 #Sentinela
        for nucleotideo in gene.upper():
            self.bit_string <<= 2 #Desloca dois bits para a esquerda
            if nucleotideo == 'A':
                self.bit_string |= 0b00
            elif nucleotideo == 'C':
                self.bit_string |= 0b01
            elif nucleotideo == 'G':
                self.bit_string |= 0b10
            elif nucleotideo == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotídeo: {}".format(nucleotideo))
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): # -1 para excluir a sentinela
            bits: int = self.bit_string >> i & 0b11 #Obtém apenas 2 bits relevantes
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1] #Inverte a string
    

    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    original:str = "TAAAACGTAGCAAGTCGTAACGATCAGTAGTAC" * 100
    print("Original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))