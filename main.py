## main function for ucm badge sort
## takes input files, returns a sorted list of courses that appear most in input files
## format for input files is a list of classes, checks for duplicates.
## prints classes with most duplicates, with classes fulfilling most requirements at bottom.
## Christopher Ahrens, 2019

import sys

FILES = []

for i in range(len(sys.argv)-1):
    FILES.append( open(str(sys.argv[i+1]), 'r') )

COURSES = []

for file in FILES:
    for line in file:
        entry = line.strip().split('\t')
        hasDuplicate = False
        for course in COURSES:
            if course[0] == entry:
                course[1] += 1
                hasDuplicate = True
        if not hasDuplicate:
            COURSES.append([entry, 1])

COURSES.sort(key=lambda tup: tup[1])

for i in COURSES:
    if(i[1] == 1):
        print(i[1], "badge  -", i[0][0])
    else:
        print(i[1], "badges -", i[0][0])