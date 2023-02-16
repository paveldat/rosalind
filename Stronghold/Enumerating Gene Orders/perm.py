from itertools import permutations


def main():
    try:
        with open('rosalind_perm.txt', 'r') as f:
            n = f.readlines()[0].strip()
        if not (n.isdigit() and 0 < int(n) <= 7):
            error = f'The value of n must be in the range [1, 7].\
                      But `{n}` was given.'
            raise ValueError(error)
        perm = list(permutations(list(range(1, int(n) + 1))))
        print(len(perm))
        for i in perm:
            for j in i:
                print(j, end=" ")
            print()
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    main()
