def main():
    with open('rosalind_revc.txt', 'r') as f:
        revc = f.readlines()[0].strip()
    print(revc[::-1].translate(str.maketrans('ACGT', 'TGCA')))


if __name__ == '__main__':
    main()
