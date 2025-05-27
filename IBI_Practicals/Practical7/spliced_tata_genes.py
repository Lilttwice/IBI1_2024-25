import re
# This script identifies genes with specific splice donor/acceptor combinations and TATA box patterns.
combo = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").strip().upper()
# Validate input
# Check if the input is one of the valid combinations
# GTAG, GCAG, or ATAC
# If not, print an error message and exit
if combo not in ['GTAG', 'GCAG', 'ATAC']:
    print("Invalid input. Please choose one of GTAG, GCAG, ATAC.")
    exit()

donor = combo[:2]
acceptor = combo[2:]

tata_pattern = re.compile(r'TATA[AT]A[AT]')

# The gene names are extracted from the header lines
# The sequences are concatenated into a single string for each gene
# The script then searches for the specified splice donor/acceptor combinations
# and TATA box patterns in the sequences
# The script uses regular expressions to find TATA box patterns
# The script also checks for the presence of splice donor/acceptor combinations
genes = []
current_gene = None
current_sequence = []
# Read the FASTA file and extract gene sequences
# The script reads the file, extracts gene names and sequences, and stores them in a list
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    for line in f:
        line = line.strip()
        # Each gene is represented by a header line starting with '>', followed by lines containing the sequence
        if line.startswith('>'):
            if current_gene is not None:
                genes.append((current_gene, ''.join(current_sequence)))
                current_sequence = []
            gene_info = line[1:]
            gene_name = gene_info.split()[0].split(':')[-1]
            current_gene = gene_name
        else:
            current_sequence.append(line)
    if current_gene is not None:
        genes.append((current_gene, ''.join(current_sequence)))

output_genes = []
# Iterate through the genes and check for splice donor/acceptor combinations and TATA box patterns
# The script checks for the presence of splice donor/acceptor combinations
for gene_name, seq in genes:
    donor_positions = []
    acceptor_positions = []
    for i in range(len(seq) - 1):
        if seq[i:i+2] == donor:
            donor_positions.append(i)
        if seq[i:i+2] == acceptor:
            acceptor_positions.append(i)
    
    has_splice = False
    for i in donor_positions:
        for j in acceptor_positions:
            if j >= i + 2:
                has_splice = True
                break
        if has_splice:
            break
    if not has_splice:
        continue
    
    tata_count = len(tata_pattern.findall(seq))
    if tata_count == 0:
        continue
    
    output_genes.append((gene_name, tata_count, seq))

output_filename = f"{combo}_spliced_genes.fa"
# Write the output to a new FASTA file

with open(output_filename, 'w') as f:
    for gene_name, count, seq in output_genes:
        f.write(f'>{gene_name}_{count}\n')
        f.write(f'{seq}\n')