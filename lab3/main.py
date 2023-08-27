from randgrid import Grid
from queue import PriorityQueue
import time
import ucs_ids
import bfs_dfs

class Testing:
    
    def __init__(self) -> None:
        self.g = Grid()
        self.target = self.g.flatten(self.g.target())
        self.matrix = self.g.generate()
        self.posx, self.posy = self.g.position(self.matrix)
        
        self.bfs_dfs = bfs_dfs.Solution()
        self.ucs_ids = ucs_ids.Solution()
    
    def benchmark(self, epoch = 10):
        print("Benchmarking...")
        result = []
        score = [0, 0, 0, 0]
        for i in range(epoch):
            # generate new matrix
            self.matrix = self.g.generate()
            self.posx, self.posy = self.g.position(self.matrix)

            max_queue = PriorityQueue()

            self.bfs_dfs.search(self.matrix, self.posx, self.posy, "BFS")
            if not self.bfs_dfs.bfs_result_found:
                result.append([0, 0, 0, 0, False])
                print(f"Epoch {i+1} completed")
                continue

            self.bfs_dfs.search(self.matrix, self.posx, self.posy, "DFS")
            self.ucs_ids.search(self.matrix, self.posx, self.posy, self.ucs_ids.h0)
            ucs_step_count = self.ucs_ids.step_count
            self.ucs_ids.search(self.matrix, self.posx, self.posy, self.ucs_ids.h1, quite=True)

            result.append(
                [self.bfs_dfs.dfs_step_count, self.bfs_dfs.bfs_step_count, ucs_step_count, self.ucs_ids.step_count, True])
            
            score[result[i].index(min(result[i][0:4]))] += 1

            print(f"Epoch {i+1} completed")

        print(f"\n----RESULTS----[{epoch} epochs]")
        print("DFS\tBFS\tUFS\tIDS\tresult")
        for i in range(epoch):
            print(
                f"{result[i][0]}\t{result[i][1]}\t{result[i][2]}\t{result[i][3]}\t{result[i][4]}")

        print("\n----SCORES-----")
        print(
            f"DFS: {score[0]}\nBFS: {score[1]}\nUFS: {score[0]}\nIDS: {score[1]}")

if __name__ == '__main__':
    t = Testing()
    t.benchmark(50)