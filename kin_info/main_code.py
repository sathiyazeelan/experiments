import os

filepath = "E:/projects/git/experiments/kin_info/kin_coverage.tsv"
filepath_test = "E:/projects/git/experiments/kin_info/kin_coverage_test.tsv"
file_open = open(filepath, 'r')
header = file_open.readline()
file_content = file_open.readlines()
print(file_content) # prints whole file as single list with multi elements
for line in file_content:
    print(line.split('\t')) # prints each line as each list
for line in file_content:
    print(line.split('\t')[0]) # prints 1st column as strings in each line
for line in file_content:
    print(line.split('\t')[0], end = ' ') # prints in one line
print(os.getcwd())
