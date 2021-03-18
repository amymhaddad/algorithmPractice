"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""

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
