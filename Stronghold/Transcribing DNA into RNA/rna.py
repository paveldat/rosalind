def main():
    with open('rosalind_rna.txt', 'r') as f:
        rna = f.readlines()[0].strip()
    print(rna.replace('T', 'U'))


if __name__ == '__main__':
    main()
