# Description: This script is used to find the largest intron length in a gene sequence.
import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

print("gene sequence：", seq)

# 使用正则表达式查找所有GT和AG的位置
gt_positions = [m.start() for m in re.finditer(r'GT', seq)]
ag_positions = [m.start() for m in re.finditer(r'AG', seq)]

max_length = 0

for gt in gt_positions:
    for ag in ag_positions:
        if ag >= gt + 1:
            current_length = ag - gt + 2
            if current_length > max_length:
                max_length = current_length

print("The largest intron length is:", max_length)