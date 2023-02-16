from rna_codon_table import RNA_CODON_TABLE


def rna_into_protein(rna: str) -> str:
    """
    Translating RNA into Protein.

    Args:
        * rna - RNA string.

    Returns:
        * The protein string encoded by `rna`.
    """

    protein = ''
    if len(rna) % 3 == 0:
        for i in range(0, len(rna), 3):
            codon = RNA_CODON_TABLE[rna[i:i + 3]]
            if codon == 'Stop':
                break
            protein += codon
    return protein


def main():
    with open('rosalind_prot.txt', 'r') as f:
        rna = f.readlines()[0].strip()
    print(rna_into_protein(rna))


if __name__ == '__main__':
    main()
