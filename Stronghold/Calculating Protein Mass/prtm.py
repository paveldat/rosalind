from mass_table import MONOISOTOPIC_MASS_TABLE


def calculate_protein_mass(protein: str) -> int:
    """
    Calculating Protein Mass.

    Args:
        * protein - A protein string of length at most 1000 aa.

    Returns:
        * The total weight of `protein`.
    """

    weight = 0
    for i in protein:
        weight += MONOISOTOPIC_MASS_TABLE[i]
    return round(weight, 3)


def main():
    with open('rosalind_prtm.txt', 'r') as f:
        protein = f.readlines()[0].strip()
    print(calculate_protein_mass(protein))


if __name__ == '__main__':
    main()
