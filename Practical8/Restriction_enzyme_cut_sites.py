def find_restriction_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = set('ACGT')
    if not set(dna_sequence).issubset(valid_nucleotides) or not set(enzyme_sequence).issubset(valid_nucleotides):
        raise ValueError("Both sequences should only contain ACGT nucleotides")
    sites = []
    len_enzyme = len(enzyme_sequence)
    for i in range(len(dna_sequence) - len_enzyme + 1):
        if dna_sequence[i:i + len_enzyme] == enzyme_sequence:
            sites.append(i)
    return sites

# example
try:
    dna = "ACGTACGT"
    enzyme = "ACGT"
    sites = find_restriction_sites(dna, enzyme)
    print(f"The restriction enzyme cut sites are: {sites}")
except ValueError as e:
    print(e)