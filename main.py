## main function for ucm badge sort
## takes input files, returns a sorted list of courses that appear most in input files
## format for input files is a list of classes of the format 'DEPT001', i.e. CSE100
## Christopher Ahrens and Wyssanie Chomsin, 2019

import sys

FILES = []

for i in range(len(sys.argv)-1):
    FILES.append( open(str(sys.argv[i+1]), 'r') )

COURSES = []

for file in FILES:
    for line in FILES[file]:
        entry = line.strip().split('\t')
        hasDuplicate = False
        for course in COURSES:
            if course[0] == entry:
                course[1] += 1
                hasDuplicate = True
        if not hasDuplicate:
            COURSES.append([entry, 1])


for i in COURSES:
    print(i)