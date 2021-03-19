"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""
from collections import Counter

def hungry_students(students, sandwiches):
    return (students.count(1) == len(students) or students.count(0) == len(students)) and students[0] != sandwiches[0]
    

def count_students(students, sandwiches):
    while True:
        if students == []:
            return 0
        elif hungry_students(students, sandwiches):
            return len(students)
        else:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                end_queue = students.pop(0)
                students.append(end_queue)

# print(count_students(students, sandwiches))

def count_students_v2(students, sandwiches):

    students_count = Counter(students)
    sandwiches_count = Counter(sandwiches)
    print(students_count) 
    for st, count in students_count.items():
        #import pdb; pdb.set_trace()
        if st in sandwiches_count:
            students_count[st] = count -1
        
    return students_count             
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
# students = [1,1,0,0]
# sandwiches = [0,1,0,1]
print(count_students_v2(students, sandwiches))

