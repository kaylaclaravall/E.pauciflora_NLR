# python maker_upper.py input.fasta > output.fasta

import sys

fastaFileName = sys.argv[1]
fasta_list = []
with open(fastaFileName) as fastaFile:
    fasta_list = fastaFile.read().splitlines()

new_list = []

for entry in fasta_list:
    if ">" in entry:
        new_list.append(entry)
    else:
        new_list.append(entry.upper())

for entry in new_list:
    print(entry)
