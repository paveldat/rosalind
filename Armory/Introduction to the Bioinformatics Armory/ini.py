from Bio.Seq import Seq


def main():
    with open('rosalind_ini.txt', 'r') as f:
        ini = Seq(f.readlines()[0].strip())
    print(*map(ini.count, "ACGT"))


if __name__ == '__main__':
    main()
