"""
https://www.algoexpert.io/questions/Breadth-first%20Search
"""

from collections import deque

tree = {
   1: [3, 4, 7],
   2: [],
   3: [2],
   4: [6],
   5: [],
   6: [5],
   7: [],
}

root = 1


def bfs(tree, root):

    que = deque()
    que.append(root)
    results = []    

    while que:
        item = que.popleft()
        results.append(item)

        for connection in tree[item]:
            que.append(connection)
    return results

print(bfs(tree, root))
