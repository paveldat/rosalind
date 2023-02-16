def main():
    with open('rosalind_dna.txt', 'r') as f:
        dna = f.readlines()[0].strip()
    print(*map(dna.count, "ACGT"))


if __name__ == '__main__':
    main()
