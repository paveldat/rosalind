def rabbits(n: int, k: int) -> int:
    """
    Counting the total number of rabbit pairs.

    Args:
        * n - month
        * k - litter of rabbit pairs
    Returns:
        * The total number of rabbit pairs that will be present after n
            months, if we begin with 1 pair and in each generation,
            every pair of reproduction-age rabbits produces a litter
            of k rabbit pairs (instead of only 1 pair).
    """

    if n == 0 or n == 1:
        return n
    else:
        return rabbits(n - 1, k) + k * rabbits(n - 2, k)


def main():
    with open('rosalind_fib.txt', 'r') as f:
        n, k = [int(value) for value in next(f).split()]
    try:
        if not (0 <= n <= 40 and 0 <= k <= 5):
            raise ValueError(f'The value of n must be in the range [1, 40].\
                               The value of k must be in the range [1, 5].\
                               But n={n} and k={k} were given.')
        print(rabbits(n, k))
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    main()
