# python coiled_counter.py input_aa.fasta

import sys

fastaFileName = sys.argv[1]

fasta_list = []

with open(fastaFileName) as fastaFile:
    fasta_list = fastaFile.read().splitlines()


count = 0
for entry in fasta_list:
	if ">" in entry:
		count += 1

print("There are {} total sequences".format(count))

amino_list = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

coiled_count = 0

for entry in fasta_list:
	for amino in amino_list:
		if "LDD{}W".format(amino) in entry:
			coiled_count += 1

print("There are {} total coiled-coil sequences".format(coiled_count))
