"""
https://www.algoexpert.io/questions/Task%20Assignment
"""



def task_assignment(k, tasks):
    original = {i : duration for i, duration in enumerate(tasks)}
   # {0: 1, 1: 3, 2: 5, 3: 3, 4: 1, 5: 4}

    tasks.sort()
    
    lower = 0
    upper = len(tasks) -1

    task_assignments = []
    #[[1, 4], [3, 1], [5, 3]]
    
    for i in range(k):
#        import pdb; pdb.set_trace() 
            
        task_assignments.extend([[original[lower], original[upper]]])
        lower += 1
        upper -= 1
    return task_assignments

k = 3 
tasks = [1, 3, 5, 3, 1, 4]

print(task_assignment(k, tasks))

#Get the original indexes from the tasks array that are stored in original 
#and insert each original index into the task_assignment 
