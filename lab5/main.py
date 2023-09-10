from randgrid import Grid
import hill_climbing
import time
import math
import random

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
        self.optimal_path_distance = 0
        self.T = MAX_POSSIBLE_STEP
        self.alpha = 0.9999
        self.Tmin = 0.00001

    def search(self, matrix, x, y , hurestic, neighbourhood, cooling_function, probability ):
        self.parent = {self.g.flatten(matrix) : None }
        self.step_count, self.result_found = 0, False
        solution = matrix
        posx, posy = x,y
        cost = hurestic(solution)

        best_solution = solution
        best_cost = cost

        temp = self.T
        all_neighbours = []
        depth = 0

        while temp > self.Tmin:
            if cost == 0:
                self.result_found = True
                self.optimal_path_distance = depth
                break

            self.step_count += 1
            # choose a random neighbour
            direction = [self.g.top, self.g.bottom, self.g.right, self.g.left]
            for d in direction:
                neighbour, x, y = d(solution, posx, posy)
                if neighbour is not None and self.g.flatten(neighbour) not in self.parent:
                    # print(neighbour)
                    all_neighbours.append([neighbour, x, y, depth+1])

            # next_node = random.choice(all_neighbours)
            next_index = neighbourhood(len(all_neighbours))
            next_node = all_neighbours[next_index]
            [next_solution, x2, y2, d] = next_node
            next_cost = hurestic(next_solution)
            # all_neighbours.remove(next_node)
            all_neighbours.pop(next_index)

            delta = cost - next_cost
            if delta > 0:
                self.parent[self.g.flatten(next_solution)] = self.g.flatten(solution)
                solution = next_solution
                posx, posy, depth = x2, y2, d
                cost = next_cost
                if cost < best_cost:
                    best_solution = solution
                    best_cost = cost
            elif random.random() < probability(cost, next_cost, temp):
                self.parent[self.g.flatten(next_solution)] = self.g.flatten(solution)
                solution = next_solution
                posx, posy, depth = x2, y2, d
                cost = next_cost
            
            # cooling
            loading(self.step_count, MAX_POSSIBLE_STEP)
            # print(temp, self.step_count)
            temp = cooling_function(temp)

        return best_solution, best_cost

    def run(self, matrix, posx, posy, neighbourhood_func, cooling_func, prob_func):
        print("\nInitial matrix: ")
        self.g.display(matrix)

        print("\nTarget matrix: ")
        self.g.display(self.g.target())

        print("Running Simmulated anneling Search with heurestics ( h1 ): ")
        start = time.time()
        best_solution, best_cost = self.search(matrix, posx, posy, self.h1, neighbourhood_func, cooling_func, prob_func )
        delta = time.time() -start
        print(f"\nTotal steps visited: {self.step_count}")
        print(f"Solution Possible: {self.result_found}")
        print(f"Time taken: {delta:06f} seconds")
        print(f"Optimal Path distance: {self.optimal_path_distance}")

        print("Running Simmulated anneling Search with heurestics ( h2 ): ")
        start = time.time()
        best_solution, best_cost = self.search(matrix, posx, posy, self.h2,  neighbourhood_func, cooling_func, prob_func)
        delta = time.time() -start
        print(f"\nTotal steps visited: {self.step_count}")
        print(f"Solution Possible: {self.result_found}")
        print(f"Time taken: {delta:06f} seconds")
        print(f"Optimal Path distance: {self.optimal_path_distance}")

    def backtrace(self):
        count = 0
        node = self.target
        start = self.g.flatten(self.matrix)
        optimal_path = open("path.txt", "w")
        while node != start:
            optimal_path.write(f"{node}\n")
            count += 1
            if node not in self.parent:
                print("No parent found for node:", node)
                break 
            node = self.parent[node]
        optimal_path.close()
    
    def neighbour_function(self, l):
        return -1

    
    def h1(self, mat): # heurestic 1 ( number of displaced block )
        count = 0
        for i in range(3):
            for j in range(3):
                if mat[i][j] != self.target_mat[i][j]: 
                    count += 1
        return count
    
    def h2(self, mat):
        dict = {}
        count = 0
        for i in range(3):
            for j in range(3):
                if mat[i][j] not in dict:
                    dict[mat[i][j]] = [i, j]
                else: 
                    dict[mat[i][j]].append(i)
                    dict[mat[i][j]].append(j)
                if self.target_mat[i][j] not in dict:
                    dict[self.target_mat[i][j]] = [i, j]
                else: 
                    dict[self.target_mat[i][j]].append(i)
                    dict[self.target_mat[i][j]].append(j)

        for key in dict:
            count += abs(dict[key][0]-dict[key][2]) + abs(dict[key][1]-dict[key][3])

        return count
    
    def probability(self, fc, fn, T):
        return math.exp((fc-fn)/T)

    def cooling(self, T):
        return T*self.alpha
            


if __name__ == '__main__':
    import sys
    sol = Solution()

    if len(sys.argv) >= 2:
        input1 = sys.argv[1]
        if len(sys.argv) >= 3:
            input2 = sys.argv[2]
        
        if input1 == "input.py":
            import input
            import sys

            print("Running using input.py")
            sol.run(input.matrix, input.posx, input.posy, input.neighbour_function, input.cooling, input.probability)
            if input2 == "--compare":
                sol2 = hill_climbing.Solution()
                sol2.matrix, sol2.posx, sol2.posy = input.matrix, input.posx, input.posy
                sol2.run()
            sys.exit(0)
        if input1 == "--compare":
            try:
                epoch = int(input2)
            except:
                epoch = 1
            for i in range(epoch):
                sol1 = Solution()
                sol1.run(sol1.matrix, sol1.posx, sol1.posy, sol1.neighbour_function, sol1.cooling, sol1.probability)
                sol2 = hill_climbing.Solution()
                sol2.matrix, sol2.posx, sol2.posy = sol1.matrix, sol1.posx, sol1.posy
                sol2.run()
        else:
            print("Help : `python3 main.py [filename?] [flag?]`")
            print("Avilable flag: `--compare n`")
            print("Some example:\t`python3 main.py input.py --compare`")
            print("\t\t`python3 main.py --compare 3`")
    else:
        sol.matrix = [[2,1,8],[3, 'B', 7],[6,5,4]]
        sol.posx, sol.posy = 1, 1
        sol.run(sol.matrix, sol.posx, sol.posy, sol.neighbour_function, sol.cooling, sol.probability)
    # # sol.benchmark(20)

