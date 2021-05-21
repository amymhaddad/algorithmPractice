"""
https://www.algoexpert.io/questions/Task%20Assignment
"""



def task_assignment(k, tasks):
    task_index = {i : duration for i, duration in enumerate(tasks)}

    tasks.sort()
    
    lower = 0
    upper = len(tasks) -1

    task_assignments = []
    
    for i in range(k):
        task_assignments.append(tasks[lower])
        task_assignments.append(tasks[upper])
        #import pdb; pdb.set_trace()
        lower += 1
        upper -= 1
    return get_indices(task_assignments, task_index)


def get_indices(task_assignments, task_index):
    indices = []
    #import pdb; pdb.set_trace()
    
    for tasks in task_assignments:
        first_task = tasks[0]
        second_task = tasks[1]
        indices.extend([[task_index[first_task], task_index[second_task]]])
    return indices


k = 3 
tasks = [1, 3, 5, 3, 1, 4]

print(task_assignment(k, tasks))

#Get the task_index indexes from the tasks array that are stored in original 
#and insert each task_index index into the task_assignment 
