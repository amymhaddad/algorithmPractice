"""
https://www.algoexpert.io/questions/Depth-first%20Search
"""

graph = {
    1: [3, 4, 7],
    2: [],
    3: [2],
    4: [6],
    5: [],
    6: [5],
    7: [],
}

from collections import deque
def dfs(graph, root):
 

print(dfs(graph, 1))
#[1, 7, 4, 6, 5, 3, 2]
#[1, 3, 4, 7, 2, 6, 5]


"""
-When at a given node, add that curr node name to the final array
-For each child in its self.children array, call the depthFIrest search function on each child

"""