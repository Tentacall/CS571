from queue import LifoQueue
from randgrid import *

class DFS(Grid):
    def __init__(self):
        super().__init__()
        self.visited = set()
        self.stack = LifoQueue()
        self.targetGrid = self.target()
        self.steps = 0

    def search(self, matrix):
        self.stack.put(matrix)
        while not self.stack.empty():
            current = self.stack.get()
            if self.is_target(current):
                return True
            self.visited.add(self.flatten(current))
            self.steps += 1
            for neighbor in self.neighbors(current):
                if self.flatten(neighbor) not in self.visited:
                    self.stack.put(neighbor)
        return False
    
    def is_target(self, matrix):
        return matrix == self.targetGrid
    
    def neighbors(self, matrix):
        adj = []
        i, j = self.find_blank(matrix)
        if self.top(matrix, i, j) is not None:
            adj.append(self.top(matrix, i, j))
        if self.bottom(matrix, i, j) is not None:
            adj.append(self.bottom(matrix, i, j))
        if self.right(matrix, i, j) is not None:
            adj.append(self.right(matrix, i, j))
        if self.left(matrix, i, j) is not None:
            adj.append(self.left(matrix, i, j))
        
        return adj 