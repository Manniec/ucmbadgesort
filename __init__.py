import re #regular expression syntax/regex

#reads comma separated list of courses txt file
def readList (filename): #inputs are 'filename.txt', 
    courses = open(filename, 'r', encoding="utf-8") # r = readfile
    List = []
    for line in courses:
        #data = line.strip().strip(',').replace(' ',',').split(',')
        #data = re.split('(\d+)',line.strip().strip(','))
        data = re.split('[, ]',line.strip().strip(','))
        #remove begining and ending whitespace and ',' char, if any & split by ',' or ' '
        List.extend(data) #elements of data are added to List
    courses.close()
    List2 = []
    for i in range(len(List)): #breaks apart longer terms like 'ANTH130' to 'ANTH', '130'
        if len(List[i]) > 4:
            List2.extend(re.findall('\d*\D+', List[i].strip()))
        else:
            List2.append(List[i]) #List2 is now a list of departments and course numbers
    courseList = []
    for i in List2: #Concatinate DEPT to course number -> DEPT001
        if i.isalpha(): #if DEPT set to dept variable and concatinate to following course numbers
            dept = i
        else:
            courseList.append(dept + i)


    return courseList

##test code##
for i in readList('crossroads.txt'):
    print(i)
