from enum import IntEnum
from typing import Tuple, List

Nucleotide = IntEnum("Nucleotide", ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

geneStr: str = "ACGAGTCTACGACGCAACGTATAGATAGCATAATAGCATGA"

def stringToGene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene

def linearSearch(gene, keyCodon) -> bool:
    for codon in gene:
        if codon == keyCodon:
            return True
    return False

def binarySearch(gene, keyCodon) -> bool:
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < keyCodon:
            low = mid + 1
        elif gene[mid] > keyCodon:
            high = mid - 1
        else:
            return True
    return False

myGene: Gene = stringToGene(geneStr)
myGeneSorted = sorted(myGene)

ACG = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
CGA = (Nucleotide.C, Nucleotide.G, Nucleotide.A)

print(linearSearch(myGene, ACG))
print(linearSearch(myGene, CGA))
print(binarySearch(myGene, ACG))
print(binarySearch(myGene, CGA))
