from Bio import Entrez


EMAIL = 'paveldat@github.com'
DB = 'nucleotide'


def genbank(genus: str, start_date: str, end_date: str) -> str:
    """
    GenBank.

    Args:
        * genus - The genus name.
        * start_date - Search start date.
        * end_date - Search end date.

    Returns:
        * The number of Nucleotide GenBank entries for the given genus that
          were published between the dates specified.
    """

    Entrez.email = EMAIL
    term = f'{genus}[Organism] AND ({start_date}[Publication Date] :\
             {end_date}[Publication Date])'
    handle = Entrez.esearch(db=DB, term=term)
    record = Entrez.read(handle)
    return record['Count']


def main():
    with open('rosalind_gbk.txt', 'r') as f:
        genus, start_date, end_date = f.read().splitlines()
    print(genbank(genus, start_date, end_date))


if __name__ == '__main__':
    main()
