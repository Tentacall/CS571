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

        # self.bfs_result_found = False
        # self.bfs_step_count = 0

        # self.dfs_result_found = False
        # self.dfs_step_count = 0
        
        # self.ucs_result_found = False
        # self.ucs_step_count = 0

        # self.ids_result_found = False
        # self.ids_step_count = 0
    
    def run(self):
        pass
    
    def benchmark(self, epoch = 10):
        print("Benchmarking...")
        result = [[], [], [], [], []]
        score = [0, 0, 0, 0]
        for i in range(epoch):
            self.matrix = self.g.generate()
            self.posx, self.posy = self.g.position(self.matrix)

            self.bfs_dfs.search(self.matrix, self.posx, self.posy, "DFS")
            self.bfs_dfs.search(self.matrix, self.posx, self.posy, "BFS")
            result.append(
                [self.bfs_dfs.dfs_step_count, self.bfs_dfs.bfs_step_count, self.bfs_dfs.dfs_result_found])
            if self.bfs_dfs.dfs_step_count < self.bfs_dfs.bfs_step_count:
                score[0] += 1
            if self.bfs_dfs.dfs_step_count > self.bfs_dfs.bfs_step_count:
                score[1] += 1
            print(f"Epoch {i+1} completed")

        print(f"\n----RESULTS----[{epoch} epochs]")
        print("DFS\tBFS\tUFS\tIDS\tresult")
        for i in range(epoch):
            print(
                f"{result[i][0]}\t{result[i][1]}\t{result[i][2]}\t{result[i][3]}\t{result[i][4]}")

        print("--------------")
        print("Average\nDFS\tBFS\tUFS\nIDS")
        print(
            f"{sum([x[0] for x in result]) / epoch}\t{sum([x[1] for x in result]) / epoch}\t{sum([x[2] for x in result]) / epoch}\t{sum([x[3] for x in result]) / epoch}")

        print("\n----SCORES-----")
        print(
            f"DFS: {score[0]}\nBFS: {score[1]}\nUFS: {score[0]}\nIDS: {score[1]}")
