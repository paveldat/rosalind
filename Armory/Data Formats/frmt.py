from Bio import Entrez, SeqIO


EMAIL = 'paveldat@github.com'
DB = 'nucleotide'
RETTYPE = 'fasta'


def data_formats(ids: list) -> str:
    """
    Data Formats.

    Args:
        * ids - List of the GenBank entry IDs.

    Returns:
        * The shortest of the strings associated with the IDs in FASTA format.
    """

    Entrez.email = EMAIL
    handle = Entrez.efetch(db=DB, id=ids, rettype=RETTYPE)
    records = list(SeqIO.parse(handle, RETTYPE))
    [min_index] = [i for i in range(len(records))
                   if len(records[i]) == min([len(record.seq)
                                              for record in records])]
    handle = Entrez.efetch(db=DB, id=ids, rettype=RETTYPE)
    return handle.read().strip().split('\n\n')[min_index]


def main():
    try:
        with open('rosalind_frmt.txt') as f:
            ids = f.read().strip().split()
        if not 0 <= len(ids) <= 10:
            raise ValueError(f'The length of IDs is incorrect.\
                               The length of IDs list must be `<= 10`.\
                               Got length {len(ids)}.')
        print(data_formats(ids))
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    main()
