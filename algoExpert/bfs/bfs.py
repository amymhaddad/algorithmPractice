"""
https://www.algoexpert.io/questions/Breadth-first%20Search
"""

from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):

        que = deque()
        que.append(self)

        while que:
            current = que.popleft()
            array.append(current.name)
            for child in current.children:
                que.append(child)
        return array
