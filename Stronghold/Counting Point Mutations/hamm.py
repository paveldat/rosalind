def count_point_mtations(dna_1: str, dna_2: str) -> int:
    """
    Counting Point Mutations.

    Args:
        * dna_1 - first DNA.
        * dna_2 - second DNA.

    Returns:
        * The number of corresponding symbols that differ in dna_1 and dna_2.
    """

    count = 0
    for i in range(len(dna_1)):
        if dna_1[i] != dna_2[i]:
            count += 1
    return count


def main():
    with open('rosalind_hamm.txt', 'r') as f:
        dna_1, dna_2 = f.read().splitlines()
    try:
        if len(dna_1) != len(dna_2):
            raise ValueError(f'DNA lengths are different.\
                               Length of the DNA_1={len(dna_1)},\
                               length of the DNA_2={len(dna_2)}.')
        print(count_point_mtations(dna_1, dna_2))
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    main()
