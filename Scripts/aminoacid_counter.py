# aminoacid_counter.py

# To run this script enter the following into command line:
# python aminoacid_counter.py < input_amino_acid.fasta

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

count = int(len(unfiltered_list)) / 2
print("There are {} total sequences retained.".format(count))

keep_seq = []

# first filter
for index in range(len(unfiltered_list)):
    if any(motif in unfiltered_list[index] for motif in ("GKT", "LDD")):
        keep_seq.append(index - 1)
        keep_seq.append(index)


filtered_list = []

for x in keep_seq:
    filtered_list.append(unfiltered_list[x])

count = int(len(filtered_list)) / 2
print("There are {} GKT and/or LDD sequences retained.".format(count))

last_keep = []

# second filter
for index in range(len(filtered_list)):
    if "LDD" in filtered_list[index]:
        if "GKT" in filtered_list[index]:
            last_keep.append(index - 1)
            last_keep.append(index)

final_list = []

for x in last_keep:
    final_list.append(filtered_list[x])


count = int(len(final_list)) / 2
print("There are {} GKT+LDD sequences retained.".format(count))




#coiled-coil type NB-ARC

LDDAW = 0
LDDRW = 0
LDDNW = 0
LDDDW = 0
LDDCW = 0
LDDQW = 0
LDDEW = 0
LDDGW = 0
LDDHW = 0
LDDIW = 0
LDDLW = 0
LDDKW = 0
LDDMW = 0
LDDFW = 0
LDDPW = 0
LDDSW = 0
LDDTW = 0
LDDWW = 0
LDDYW = 0
LDDVW = 0


for entry in final_list:
    if "LDDAW" in entry:
        LDDAW += 1
    if "LDDRW" in entry:
        LDDRW += 1
    if "LDDNW" in entry:
        LDDNW += 1
    if "LDDDW" in entry:
        LDDDW += 1
    if "LDDCW" in entry:
        LDDCW += 1
    if "LDDQW" in entry:
        LDDQW += 1
    if "LDDEW" in entry:
        LDDEW += 1
    if "LDDGW" in entry:
        LDDGW += 1
    if "LDDHW" in entry:
        LDDHW += 1
    if "LDDIW" in entry:
        LDDIW += 1
    if "LDDLW" in entry:
        LDDLW += 1
    if "LDDKW" in entry:
        LDDKW += 1
    if "LDDMW" in entry:
        LDDMW += 1
    if "LDDFW" in entry:
        LDDFW += 1
    if "LDDPW" in entry:
        LDDPW += 1
    if "LDDSW" in entry:
        LDDSW += 1
    if "LDDTW" in entry:
        LDDTW += 1
    if "LDDWW" in entry:
        LDDWW += 1
    if "LDDYW" in entry:
        LDDYW += 1
    if "LDDVW" in entry:
        LDDVW += 1


print("There are {} LDDAW".format(LDDAW))
print("There are {} LDDRW".format(LDDRW))
print("There are {} LDDNW".format(LDDNW))
print("There are {} LDDDW".format(LDDDW))
print("There are {} LDDCW".format(LDDCW))
print("There are {} LDDQW".format(LDDQW))
print("There are {} LDDEW".format(LDDEW))
print("There are {} LDDGW".format(LDDGW))
print("There are {} LDDHW".format(LDDHW))
print("There are {} LDDIW".format(LDDIW))
print("There are {} LDDLW".format(LDDLW))
print("There are {} LDDKW".format(LDDKW))
print("There are {} LDDMW".format(LDDMW))
print("There are {} LDDFW".format(LDDFW))
print("There are {} LDDPW".format(LDDPW))
print("There are {} LDDSW".format(LDDSW))
print("There are {} LDDTW".format(LDDTW))
print("There are {} LDDWW".format(LDDWW))
print("There are {} LDDYW".format(LDDYW))
print("There are {} LDDVW".format(LDDVW))
