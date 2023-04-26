import os

filepath = "E:/projects/git/experiments/kin_info/kin_coverage.tsv"
filepath_test = "E:/projects/git/experiments/kin_info/kin_coverage_test.tsv"
# file_open = open(filepath, 'r')
# header = file_open.readline()
# file_content = file_open.readlines()
# for line in file_content:
# 	parents = (line.split('\t')[3].replace(',', ';'))
	
# print(header.split('\t'))
# print(os.getcwd())

with open(filepath, 'r') as f:
    lines = []
    # Read the file into a list of lists
    for line in f:
        row = line.strip().split('\t')
        lines.append(row)
    # print(lines)

header = lines[0]
header.insert(3, 'New Column')
for row in lines[1:]:
    row.insert(3, '')
    print(row)
# print(header)
with open(filepath_test, 'w') as f:
    # Write the header
    f.write('\t'.join(header) + '\n')
    # Write the rows
    for row in lines[1:]:
        f.write('\t'.join(row) + '\n')

