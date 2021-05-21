"""
https://www.algoexpert.io/questions/Task%20Assignment
"""


def task_assignment(k, tasks):
    task_index = {i: duration for i, duration in enumerate(tasks)}

    tasks.sort()

    lower, upper = 0, len(tasks) - 1
    task_assignments = []

    for i in range(k):
        task_assignments.extend([[tasks[lower], tasks[upper]]])
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
                task_index = original_tasks.index(task)
                pair.append(task_index)
                original_tasks[task_index] = None
        indices.extend([pair])
    return indices
