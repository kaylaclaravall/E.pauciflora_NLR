# python filter_fasta.py input_aa.fasta > output_aa.fasta

import sys

fastaFileName = sys.argv[1]

fasta_list = []

with open(fastaFileName) as fastaFile:
    fasta_list = fastaFile.read().splitlines()

GKT = 0
GKS = 0
both = 0
index_list = []

for index in range(len(fasta_list)):
	if "GKT" in fasta_list[index]:
		if "GKS" not in fasta_list[index]:
			if "LDD" in fasta_list[index]:
				GKT += 1
				index_list.append(index)

for index in range(len(fasta_list)):
	if "GKS" in fasta_list[index]:
		if "GKT" not in fasta_list[index]:
			if "LDD" in fasta_list[index]:
				GKS += 1
				index_list.append(index)

for index in range(len(fasta_list)):
	if "GKS" in fasta_list[index]:
		if "GKT" in fasta_list[index]:
			if "LDD" in fasta_list[index]:
				both += 1
				index_list.append(index)

#print("There are {} GK T/S + LDD sequences".format(GKT + GKS + both))

out_list = []

for index in index_list:
	out_list.append(fasta_list[index - 1])
	out_list.append(fasta_list[index])

for entry in out_list:
	print(entry)
