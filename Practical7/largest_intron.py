seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Identify the lagrest intron
intron = seq.split('T')
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

gt_positions = []
ag_positions = []

for i in range(len(seq) - 1):
    if seq[i] == 'G' and seq[i+1] == 'T':
        gt_positions.append(i)
    if seq[i] == 'A' and seq[i+1] == 'G':
        ag_positions.append(i)

max_length = 0

for gt_i in gt_positions:
    for ag_j in ag_positions:
        if ag_j >= gt_i + 1:
            current_length = ag_j - gt_i + 2
            if current_length > max_length:
                max_length = current_length

print(max_length)