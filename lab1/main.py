from randgrid import Grid
import queue

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
        self.target = self.g.flatten(self.g.target())
        self.matrix = self.g.generate()
        self.posx, self.posy = self.g.position(self.matrix)

        self.bfs_visited = {}
        self.bfs_queue = queue.Queue()
        self.bfs_result_found = False
        self.bfs_step_count = 0

        self.dfs_visited = {}
        self.dfs_queue = queue.LifoQueue()
        self.dfs_result_found = False
        self.dfs_step_count = 0

    def search(self, matrix, x, y, visited ,queue, result_found, step_count ):
        queue.put((matrix, x, y))
        while not queue.empty() and not result_found:
            mat, x, y = queue.get()
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
                    queue.put((mat2, x2, y2))
            loading(step_count, MAX_POSSIBLE_STEP)

        print(f"\nTotal steps visited: {step_count}")
        print(f"Solution Possible: {result_found}")

    def run(self):
        print("\nInitial matrix: ")
        self.g.display(self.matrix)

        print("\nTarget matrix: ")
        self.g.display(self.g.target())
        
        print("Running DFS: ")
        self.search(self.matrix, self.posx, self.posy, self.dfs_visited, self.dfs_queue, self.dfs_result_found, self.dfs_step_count)

        print("Running BFS: ")
        self.search(self.matrix, self.posx, self.posy, self.bfs_visited, self.bfs_queue, self.bfs_result_found, self.bfs_step_count)

if __name__ == '__main__':
    sol = Solution()
    sol.run()
