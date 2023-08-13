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

    def dfs(self):
        pass

    def bfs(self, matrix, x, y):
        self.bfs_queue.put((matrix, self.posx, self.posy))
        while not self.bfs_queue.empty() and not self.bfs_result_found:
            mat, x, y = self.bfs_queue.get()
            flat = self.g.flatten(mat)
            if flat in self.bfs_visited:
                continue

            self.bfs_step_count += 1
            self.bfs_visited[flat] = True

            if flat == self.target:
                self.bfs_result_found = True
                break

            operations = [self.g.top, self.g.bottom, self.g.right, self.g.left]
            for op in operations:
                mat2, x2, y2 = op(mat, x, y)
                if mat2 is not None:
                    self.bfs_queue.put((mat2, x2, y2))
            loading(self.bfs_step_count, MAX_POSSIBLE_STEP)

        print(f"\nTotal steps visited: {self.bfs_step_count}")
        print(f"Solution Possible: {self.bfs_result_found}")


if __name__ == '__main__':
    sol = Solution()
    print("\nInitial matrix: ")
    sol.g.display(sol.matrix)
    # sol.matrix = [[7, 4, 1], [8, 5, 2], ['B', 6, 3]]
    # sol.posx, sol.posy = 2, 0
    print("Running BFS: ")
    sol.bfs(sol.matrix, sol.posx, sol.posy)
