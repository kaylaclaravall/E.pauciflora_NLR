# headers_to_bed.py

# Enter the following code into command line to run this script:
# python headers_to_bed.py headers.txt > output.bed

import sys

headersFileName = sys.argv[1]
headers_list = []
with open(headersFileName) as headersFile:
    headers_list = headersFile.read().splitlines()


bed_list = []

for entry in headers_list:
    temp_stringV = ""
    temp_stringN = ""
    temp_stringS = ""
    temp_index1 = 0
    temp_index2 = 0
    temp_index3 = 0
    temp_index4 = 0
    for index in range(len(entry)):
        if entry[index] == ">":
            temp_index1 += int(index)
        if entry[index] == ":":
            temp_index2 += int(index)
        if entry[index] == "(":
            temp_index3 += int(index)
        if entry[index] == ")":
            temp_index4 += int(index)
    for btwn in range(temp_index1 + 1, temp_index2):
        temp_stringV += entry[btwn]
    bed_list.append(temp_stringV)
    for btwn in range(temp_index2 + 1, temp_index3):
        temp_stringN += entry[btwn]
    temp_stringN1 = ""
    temp_stringN2 = ""
    for index in range(len(temp_stringN)):
        if temp_stringN[index] == "-":
            for btwn in range(0, index):
                temp_stringN1 += temp_stringN[btwn]
            for btwn in range(index + 1, len(temp_stringN)):
                temp_stringN2 += temp_stringN[btwn]
    bed_list.append(int(temp_stringN1) - 1000)
    bed_list.append(int(temp_stringN2) + 1000)
    for btwn in range(temp_index3 + 1, temp_index4):
        temp_stringS += entry[btwn]
    bed_list.append(temp_stringS)

output = ""
counter = 0
for index in range(len(bed_list)):
    if bed_list[index] != "+":
        if bed_list[index] != "-":
            output += str(bed_list[index]) + "\t"
            counter += 1
            if counter == 3:
                output += str(bed_list[index - 2]) + "\t"
                counter = 0
    if bed_list[index] == "-":
        output += "reverse" + "\t" + str(bed_list[index] + "\n")
    elif bed_list[index] == "+":
        output += "forward" + "\t" + str(bed_list[index] + "\n")


print(output)