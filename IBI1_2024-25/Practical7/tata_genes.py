import re#/Users/a1/Desktop/gitcf/Practical7/
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    for line in f:
        print(line)
        break
exit()  
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

tata_genes = []
for gene_name, seq in genes:
    if tata_pattern.search(seq):
        tata_genes.append((gene_name, seq))

with open('tata_genes.fa', 'w') as f:
    for gene_name, seq in tata_genes:
        f.write(f'>{gene_name}\n')
        f.write(f'{seq}\n')