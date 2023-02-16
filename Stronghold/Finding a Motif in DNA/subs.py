def find_motif_dna(s: str, t: str) -> list:
    """
    Finding a Motif in DNA.

    Args:
        * s - The source string for the search.
        * t - Substring for the search.

    Returns:
        * List of all locations of `t` as a substring of `s`.
    """

    locations = []
    for i in range(len(s)):
        if s[i:].startswith(t):
            locations.append(i+1)
    return locations


def main():
    with open('rosalind_subs.txt', 'r') as f:
        s, t = f.read().splitlines()
    print(' '.join(str(location) for location in find_motif_dna(s, t)))


if __name__ == '__main__':
    main()
