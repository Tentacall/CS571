from randgrid import Grid
from queue import PriorityQueue
import time

MAX_POSSIBLE_STEP = 181440
# 9! = 362880 and there are 2 disjoint set of states


def loading(current_value, total_value, bar_length=40):
    progress = min(1.0, current_value / total_value)
    arrow = '■' * int(progress * bar_length)
    spaces = ' ' * (bar_length - len(arrow))
    print(f'\r[{arrow}{spaces}] {int(progress * 100)}%', end='', flush=True)


class Solution:
    def __init__(self):
        self.g = Grid()
        self.target_mat = self.g.target()
        self.target = self.g.flatten(self.target_mat)
        self.matrix = self.g.generate()
        self.posx, self.posy = self.g.position(self.matrix)
        self.result_found, self.step_count = False, 0
        self.gval = {}
        self.optimal_path_distance = 0

    def search(self, matrix, x, y , hurestic , depth = -1, quite = False):
        result_found = False
        self.step_count = 0
        queue = PriorityQueue() # open list
        visited = {} # closed list
        # initialize
        queue.put((0, 0, x, y, matrix))
        while not queue.empty() and not result_found:
            fn,gn, x, y, mat = queue.get()
            # print(fn, gn)
            flat = self.g.flatten(mat)
            if flat in visited:
                continue

            self.step_count += 1
            visited[flat] = True

            if flat == self.target:
                result_found = True
                self.optimal_path_distance = gn
                break

            operations = [self.g.top, self.g.bottom, self.g.right, self.g.left]
            for op in operations:
                mat2, x2, y2 = op(mat, x, y)
                if mat2 is not None and ( depth == -1 or gn <= depth ):
                    fn = int(gn + 1 + hurestic(mat2,  self.target_mat ))
                    if gn <= depth:
                        fn = int( hurestic(mat2,  self.target_mat ))
                    queue.put((fn ,gn + 1, x2, y2, mat2) )
            if not quite:
                loading(self.step_count, MAX_POSSIBLE_STEP)
        self.result_found = result_found
        return visited


    def run(self):
        print("\nInitial matrix: ")
        self.g.display(self.matrix)

        print("\nTarget matrix: ")
        self.g.display(self.g.target())
        
        print("Running Uniform Cost Search: ")
        start = time.time()
        self.search(self.matrix, self.posx, self.posy, self.h0 )
        delta = time.time() -start
        print(f"\nTotal steps visited: {self.step_count}")
        print(f"Solution Possible: {self.result_found}")
        print(f"Optimal Solution Distance: {self.optimal_path_distance}")
        print(f"Time taken: {delta:06f} seconds")

        print("Running IDDFS Search: ")
        start = time.time()
        self.step_count = 0
        total_steps = 0
        for depth in range(100):
            print("Depth : ", depth)
            self.search(self.matrix, self.posx, self.posy, self.h1, depth )
            total_steps += self.step_count
            if self.result_found or self.step_count == 181440:
                break
        delta = time.time() -start
        print(f"\nTotal steps visited: {total_steps}")
        print(f"Solution Possible: {self.result_found}")
        print(f"Optimal Solution Distance: {self.optimal_path_distance}")
        print(f"Time taken: {delta:06f} seconds")

    def h0(self, mat1, mat2):
        # uniform cost search
        return 0
    
    def h1(self, mat1, mat2):
        return 181440 - self.step_count
    


if __name__ == '__main__':
    sol = Solution()
    # sol.benchmark(20)
    sol.matrix = [[2,1,8],[3, 'B', 7],[6,5,4]]
    sol.posx, sol.posy = 1, 1
    sol.run()
