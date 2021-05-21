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
        lower_val = tasks[lower]
        upper_val = tasks[upper]
        task_assignments.extend([[lower_val, upper_val]])
        # task_assignments.append(tasks[lower])
        # task_assignments.append(tasks[upper])
        lower += 1
        upper -= 1
    return get_indices(task_assignments, task_index)


def get_indices(task_assignments, task_index):
    indices = []
    
    original_tasks = [task for task in task_index.values()]
    
    for tasks in task_assignments:
        pair = []
        for task in tasks:
            if task in original_tasks:
                #import pdb; pdb.set_trace()
                task_index = original_tasks.index(task)
                pair.append(task_index) 
                original_tasks[task_index] = None
        indices.extend([pair]) 
            

    return indices


k = 3 
tasks = [1, 3, 5, 3, 1, 4]

print(task_assignment(k, tasks))

#Get the task_index indexes from the tasks array that are stored in original 
#and insert each task_index index into the task_assignment 
