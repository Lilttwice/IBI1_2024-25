import re

combo = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAC): ").strip().upper()

if combo not in ['GTAG', 'GCAG', 'ATAC']:
    print("Invalid input. Please choose one of GTAG, GCAG, ATAC.")
    exit()

donor = combo[:2]
acceptor = combo[2:]

tata_pattern = re.compile(r'TATA[AT]A[AT]')

genes = []
current_gene = None
current_sequence = []

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    for line in f:
        line = line.strip()
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

with open(output_filename, 'w') as f:
    for gene_name, count, seq in output_genes:
        f.write(f'>{gene_name}_{count}\n')
        f.write(f'{seq}\n')