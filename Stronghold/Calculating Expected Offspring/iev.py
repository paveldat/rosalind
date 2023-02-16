from genotypes import GENOTYPES


def main():
    try:
        genotype, offspring = [], 0
        with open('rosalind_iev.txt', 'r') as f:
            genotype = ([int(value) for value in next(f).split()])
        if not all(1 <= value <= 20000 for value in genotype):
            raise ValueError(f'The values must be in the range [1, 20000].')
        for i, j in enumerate(genotype):
            offspring += j * GENOTYPES[list(GENOTYPES)[i]]
        print(2 * offspring)
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    main()
