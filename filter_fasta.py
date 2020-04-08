# filter_fasta.py

# To run this script enter the following into command line:
# python filter_fasta.py < input.fasta > output.fasta

import sys

# input fasta
start_list = sys.stdin.readlines()

headers = []
# mark the index of the headers
for index in range(len(start_list)):
    if ">" in start_list[index]:
        headers.append(index)

unfiltered_list = []
temp_seq = ""

# append the headers and the sequences
for index in range(len(headers)):
    unfiltered_list.append(start_list[headers[index]])
    if headers[index] != headers[-1]:
        for btwn in range(headers[index] + 1, headers[index + 1]):
            temp_seq += start_list[btwn]
        unfiltered_list.append(temp_seq)
        temp_seq = ""


temp_seq = ""

# add the sequence for the last header
for line in start_list[headers[-1] + 1:]:
    temp_seq += line

unfiltered_list.append(temp_seq)


keep_seq = []

# first filter
for index in range(len(unfiltered_list)):
    if any(motif in unfiltered_list[index] for motif in ("GKT", "LDD")):
        keep_seq.append(index - 1)
        keep_seq.append(index)


filtered_list = []

for x in keep_seq:
    filtered_list.append(unfiltered_list[x])


last_keep = []

# second filter
for index in range(len(filtered_list)):
    if "LDD" in filtered_list[index]:
        last_keep.append(index - 1)
        last_keep.append(index)

final_list = []

for x in last_keep:
    final_list.append(filtered_list[x])

# print final_list for output fasta
for entry in final_list:
    print(entry)
