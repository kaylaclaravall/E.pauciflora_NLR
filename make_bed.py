# make_bed.py

# Enter the following code into command line to run this script:
# python make_bed.py < input_hits > output.bed

import sys

start_list = sys.stdin.readlines()

for entry in range(len(start_list)):
    if start_list[entry] == "  ------ inclusion threshold ------\n":
        upper_limit = int(entry)
    else:
        pass

# cuts off everything after the inclusion threshold
del start_list[upper_limit:]
# all nhmmer and hmmsearch standard outputs begin their list at this line
del start_list[:14]

neat_list = []

# converts the spaces between words into comma-seperated entries
for entry in start_list:
    neat_list.append(entry.split())

output = ""

for entry in neat_list:
    output += entry[3] + "\t"
    if entry != neat_list[len(neat_list) - 1]:
        if int(entry[4]) < int(entry[5]):
            output += entry[4] + "\t" + entry[5] + \
                "\t" + entry[3] + "\t" + "forward\t+\n"
        else:
            output += entry[5] + "\t" + entry[4] + \
                "\t" + entry[3] + "\t" + "reverse\t-\n"
    else:
        if int(entry[4]) < int(entry[5]):
            output += entry[4] + "\t" + entry[5] + \
                "\t" + entry[3] + "\t" + "forward\t+"
        else:
            output += entry[5] + "\t" + entry[4] + \
                "\t" + entry[3] + "\t" + "reverse\t-"


print(output)
