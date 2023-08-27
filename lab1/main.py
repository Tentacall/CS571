from randgrid import Grid
from queue import LifoQueue, Queue

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

        self.bfs_result_found = False
        self.bfs_step_count = 0

        self.dfs_result_found = False
        self.dfs_step_count = 0

    def search(self, matrix, x, y, mode="DFS"):
        result_found, step_count = False, 0
        visited = {}
        if mode == "DFS":
            queue = LifoQueue()
        else:
            queue = Queue()

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

        if mode == "BFS":
            self.bfs_result_found, self.bfs_step_count = result_found, step_count
        elif mode == "DFS":
            self.dfs_result_found, self.dfs_step_count = result_found, step_count

    def run(self):
        print("\nInitial matrix: ")
        self.g.display(self.matrix)

        print("\nTarget matrix: ")
        self.g.display(self.g.target())

        print("Running DFS: ")
        self.search(self.matrix, self.posx, self.posy,  "DFS")
        print(f"\nTotal steps visited: {self.dfs_step_count}")
        print(f"Solution Possible: {self.dfs_result_found}")

        print("\nRunning BFS: ")
        self.search(self.matrix, self.posx, self.posy, "BFS")
        print(f"\nTotal steps visited: {self.bfs_step_count}")
        print(f"Solution Possible: {self.bfs_result_found}")

    def benchmark(self, epoch):
        print("Benchmarking...")
        result = []
        score = [0, 0]
        for i in range(epoch):
            self.matrix = self.g.generate()
            self.posx, self.posy = self.g.position(self.matrix)

            self.search(self.matrix, self.posx, self.posy, "DFS")
            self.search(self.matrix, self.posx, self.posy, "BFS")
            result.append(
                [self.dfs_step_count, self.bfs_step_count, self.dfs_result_found])
            if self.dfs_step_count < self.bfs_step_count:
                score[0] += 1
            if self.dfs_step_count > self.bfs_step_count:
                score[1] += 1
            print(f"Epoch {i+1} completed")

        print(f"\n----RESULTS----[{epoch} epochs]")
        print("DFS\tBFS\tresult\tdeviation")
        for i in range(epoch):
            print(
                f"{result[i][0]}\t{result[i][1]}\t{result[i][2]}\t{result[i][0] - result[i][1]}")

        print("--------------")
        print("Average\nDFS\tBFS")
        print(
            f"{sum([x[0] for x in result]) / epoch}\t{sum([x[1] for x in result]) / epoch}")

        print("\n----SCORES-----")
        print(f"DFS: {score[0]}\nBFS: {score[1]}")


if __name__ == '__main__':
    sol = Solution()
    # sol.benchmark(100)
    sol.run()
