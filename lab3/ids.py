
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

        self.ids_result_found = False
        self.ids_step_count = 0
        self.total_step_count = 0
        
        
    def search(self, matrix, x, y):
        
        for limit in range(MAX_DEPTH):
            self.ids_result_found, self.ids_step_count = self.dfs(matrix, x, y, limit)
            self.total_step_count += self.ids_step_count
            print(f"\nDepth: {limit}")
            if(self.ids_result_found):
                break
    
    def dfs(self, matrix, x, y , limit=0 ):
        result_found, step_count = False, 0
        queue = LifoQueue() 
        visited = {}
        queue.put((matrix, x, y, limit))
        while not queue.empty() and not result_found:
            mat, x, y, l = queue.get()
            flat = self.g.flatten(mat)
            if flat in visited:
                continue

            step_count += 1
            visited[flat] = True

            if flat == self.target:
                result_found = True
                break

            operations = [self.g.top, self.g.bottom, self.g.right, self.g.left]
            for op in operations:
                mat2, x2, y2 = op(mat, x, y)
                if mat2 is not None:
                    flat = self.g.flatten(mat2)
                    if flat not in visited and l > 0:
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
        
        print("\nRunning IDS: ")
        self.search(self.matrix, self.posx, self.posy)
        print(f"\nTotal steps visited in last iteration: {self.ids_step_count}")
        print(f"Total steps visited: {self.total_step_count}")
        print(f"Solution Possible: {self.ids_result_found}")
        
if __name__ == '__main__':
    searching = IDS()
    searching.run()