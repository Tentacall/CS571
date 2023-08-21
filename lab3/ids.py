
from queue import LifoQueue,Queue
from randgrid import *

MAX_DEPTH = 1000
MAX_POSSIBLE_STEP = 181440
# 9! = 362880 and there are 2 disjoint set of states


def loading(current_value, total_value, bar_length=40):
    progress = min(1.0, current_value / total_value)
    arrow = '■' * int(progress * bar_length)
    spaces = ' ' * (bar_length - len(arrow))
    print(f'\r[{arrow}{spaces}] {int(progress * 100)}%', end='', flush=True)

class IDS:
    
    def __init__(self):
        self.g = Grid()
        self.target = self.g.flatten(self.g.target())
        self.matrix = self.g.generate()
        self.posx, self.posy = self.g.position(self.matrix)

        self.bfs_result_found = False
        self.bfs_step_count = 0
        
        self.visited = {}
        
    def bfs(self, matrix, x, y):
        result_found, step_count = False, 0
        queue = Queue()
        limit = 0

        queue.put((matrix, x, y, limit))
        while not queue.empty() and not result_found:
            mat, x, y, l = queue.get()
            flat = self.g.flatten(mat)
            if flat in self.visited:
                continue

            # step_count += 1
            # self.visited[flat] = True

            # if flat == self.target:
            #     result_found = True
            #     break
            
            result_found, count = self.dfs(mat, x, y, l)
            step_count += count
            
            if result_found:
                break

            operations = [self.g.top, self.g.bottom, self.g.right, self.g.left]
            for op in operations:
                mat2, x2, y2 = op(mat, x, y)
                if mat2 is not None:
                    flat = self.g.flatten(mat2)
                    if flat not in self.visited:
                        queue.put((mat2, x2, y2, l+1))
                    
            l += 1
            loading(step_count, MAX_POSSIBLE_STEP)

        self.bfs_result_found, self.bfs_step_count = result_found, step_count
    
    def dfs(self, matrix, x, y , limit=0 ):
        result_found, step_count = False, 0
        queue = LifoQueue() 
        queue.put((matrix, x, y, limit))
        while not queue.empty() and not result_found:
            mat, x, y, l = queue.get()
            flat = self.g.flatten(mat)
            if flat in self.visited:
                continue

            step_count += 1
            self.visited[flat] = True

            if flat == self.target:
                result_found = True
                break

            operations = [self.g.top, self.g.bottom, self.g.right, self.g.left]
            for op in operations:
                mat2, x2, y2 = op(mat, x, y)
                if mat2 is not None and (l-1)<=0:
                    flat = self.g.flatten(mat2)
                    if flat not in self.visited:
                        queue.put((mat2, x2, y2, l-1))
            loading(step_count, MAX_POSSIBLE_STEP)

        
        return result_found, step_count
    
    def run(self):
        self.matrix = [[2,1,8],[3,'B',7],[6, 5, 4]]
        self.posx = 1
        self.posy=1
        print("\nInitial matrix: ")
        self.g.display(self.matrix)

        print("\nTarget matrix: ")
        self.g.display(self.g.target())
        
        print("\nRunning BFS: ")
        self.bfs(self.matrix, self.posx, self.posy)
        print(f"\nTotal steps visited: {self.bfs_step_count}")
        print(f"Solution Possible: {self.bfs_result_found}")
        
if __name__ == '__main__':
    searching = IDS()
    searching.run()