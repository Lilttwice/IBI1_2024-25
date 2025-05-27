def find_restriction_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = set('ACGT')
    if not set(dna_sequence).issubset(valid_nucleotides) or not set(enzyme_sequence).issubset(valid_nucleotides):
        # make sure that the sequences contain only ACGT nucleotides
        raise ValueError("Both sequences should only contain ACGT nucleotides")
    sites = []
    len_enzyme = len(enzyme_sequence)
    for i in range(len(dna_sequence) - len_enzyme + 1):
        # check if the enzyme sequence is found in the dna sequence
        # if yes, record the position of the cut site
        # add 1 to the index to convert from 0-based to 1-based indexing for readable output
        # and append the position to the list of sites
        # check if the enzyme sequence is found in the dna sequence 
        if dna_sequence[i:i + len_enzyme] == enzyme_sequence:
            sites.append(i+1)
    return sites

# try an example
try:
    dna = "ACGTCGTAACGTAAA"
    enzyme = "ACGT"
    sites = find_restriction_sites(dna, enzyme)
    print(f"The restriction enzyme cut sites are: {sites}")
except ValueError as e:
    print(e+1)