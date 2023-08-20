from randgrid import Grid
from queue import PriorityQueue

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

    def search(self, matrix, x, y , hurestic ):
        result_found, step_count = False, 0
        queue = PriorityQueue() # open list
        visited = {} # closed list
        # initialize
        queue.put((0, 0, x, y, matrix))
        while not queue.empty() and not result_found:
            fn,gn, x, y, mat = queue.get()
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
                    fn = int(gn + 1 + hurestic(mat2,  self.target_mat ))
                    queue.put((fn ,gn + 1, x2, y2, mat2) )
            loading(step_count, MAX_POSSIBLE_STEP)
        self.result_found, self.step_count = result_found, step_count

    def run(self):
        print("\nInitial matrix: ")
        self.g.display(self.matrix)

        print("\nTarget matrix: ")
        self.g.display(self.g.target())
        
        print("Running A*: ")
        self.search(self.matrix, self.posx, self.posy, self.h5 )
        print(f"\nTotal steps visited: {self.step_count}")
        print(f"Solution Possible: {self.result_found}")

    def h1(self, mat1, mat2):
        return 0
    
    def h2(self, mat1, mat2):
        count = 0
        for i in range(3):
            for j in range(3):
                if mat1[i][j] != mat2[i][j]:
                    count += 1
        return count
    
    def h3(self, mat1, mat2):
        dict = {}
        count = 0
        for i in range(3):
            for j in range(3):
                if mat1[i][j] not in dict:
                    dict[mat1[i][j]] = [i, j]
                else: 
                    dict[mat1[i][j]].append(i)
                    dict[mat1[i][j]].append(j)
                if mat2[i][j] not in dict:
                    dict[mat2[i][j]] = [i, j]
                else: 
                    dict[mat2[i][j]].append(i)
                    dict[mat2[i][j]].append(j)

        for key in dict:
            count += abs(dict[key][0]-dict[key][2]) + abs(dict[key][1]-dict[key][3])

        return count
    
    def h4(self, mat1, mat2):
        dict = {}
        count = 0
        for i in range(3):
            for j in range(3):
                if mat1[i][j] not in dict:
                    dict[mat1[i][j]] = [i, j]
                else: 
                    dict[mat1[i][j]].append(i)
                    dict[mat1[i][j]].append(j)
                if mat2[i][j] not in dict:
                    dict[mat2[i][j]] = [i, j]
                else: 
                    dict[mat2[i][j]].append(i)
                    dict[mat2[i][j]].append(j)

        for key in dict:
            count += max(abs(dict[key][0]-dict[key][2]) , abs(dict[key][1]-dict[key][3]))

        return count
    
    def h5(self, mat1, mat2):
        dict = {}
        count = 0
        for i in range(3):
            for j in range(3):
                if mat1[i][j] not in dict:
                    dict[mat1[i][j]] = [i, j]
                else: 
                    dict[mat1[i][j]].append(i)
                    dict[mat1[i][j]].append(j)
                if mat2[i][j] not in dict:
                    dict[mat2[i][j]] = [i, j]
                else: 
                    dict[mat2[i][j]].append(i)
                    dict[mat2[i][j]].append(j)

        for key in dict:
            count += (abs(dict[key][0]-dict[key][2])**2 + abs(dict[key][1]-dict[key][3])**2)**(1/2)

        return count
                

    def benchmark(self, epoch):
        print("Benchmarking...")
        result = []
        score = [0,0]
        for i in range(epoch):
            self.matrix = self.g.generate()
            self.posx, self.posy = self.g.position(self.matrix)

            self.search(self.matrix, self.posx, self.posy, "DFS")
            self.search(self.matrix, self.posx, self.posy, "BFS")
            result.append([self.dfs_step_count, self.bfs_step_count, self.dfs_result_found])
            if self.dfs_step_count < self.bfs_step_count: score[0] += 1
            if self.dfs_step_count > self.bfs_step_count: score[1] += 1
            print(f"Epoch {i+1} completed")
        
        print(f"\n----RESULTS----[{epoch} epochs]")
        print("DFS\tBFS\tresult\tdeviation")
        for i in range(epoch):
            print(f"{result[i][0]}\t{result[i][1]}\t{result[i][2]}\t{result[i][0] - result[i][1]}")
        
        print("--------------")
        print("Average\nDFS\tBFS")
        print(f"{sum([x[0] for x in result]) / epoch}\t{sum([x[1] for x in result]) / epoch}")

        print("\n----SCORES-----")
        print(f"DFS: {score[0]}\nBFS: {score[1]}")


if __name__ == '__main__':
    sol = Solution()
    # sol.benchmark(20)
    sol.matrix = [[2,1,8],[3, 'B', 7],[6,5,4]]
    sol.posx, sol.posy = 1, 1
    sol.run()
