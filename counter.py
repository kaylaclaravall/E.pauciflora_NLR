# counter.py

# To run this script enter the following into command line:
# python counter.py < input.bed

import sys

start_list = sys.stdin.readlines()

neat_list = []

for entry in start_list:
    neat_list.append(entry.split())

print(len(neat_list))
