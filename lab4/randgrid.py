from typing import List
import copy
import random
GRID_SIZE = 3


class Grid:
    def __inti__(self):
        pass

    def generate(self) -> List[List[int]]:
        array = [i for i in range(1, GRID_SIZE**2)] + ['B']
        random.shuffle(array)
        matrix = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                row.append(array[i*GRID_SIZE + j])
            matrix.append(row)
        return matrix

    def display(self, matrix: List[List[int]]) -> None:
        if matrix is None:
            print("None")
            return
        for row in matrix:
            for v in row:
                print(f"{v} ", end="")
            print()
        print("------")

    def target(self) -> List[List[int]]:
        return [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]

    def flatten(self, matrix: List[List[int]]) -> str:
        res = ""
        for row in matrix:
            for v in row:
                res += str(v)
        return res

    def top(self, mat: List[List[int]], x: int, y: int):
        matrix = copy.deepcopy(mat)
        if x < 1 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
            return None, -1, -1
        matrix[x][y], matrix[x - 1][y] = matrix[x - 1][y], matrix[x][y]
        return matrix, x-1, y

    def bottom(self, mat: List[List[int]], x: int, y: int):
        matrix = copy.deepcopy(mat)
        if x < 0 or x >= GRID_SIZE - 1 or y < 0 or y >= GRID_SIZE:
            return None, -1, -1
        matrix[x][y], matrix[x + 1][y] = matrix[x + 1][y], matrix[x][y]
        return matrix, x+1, y

    def right(self, mat: List[List[int]], x: int, y: int):
        matrix = copy.deepcopy(mat)
        if x < 0 or x >= GRID_SIZE + 1 or y < 0 or y >= GRID_SIZE - 1:
            return None, -1, -1
        matrix[x][y], matrix[x][y + 1] = matrix[x][y + 1], matrix[x][y]
        return matrix, x, y+1

    def left(self, mat: List[List[int]], x: int, y: int):
        matrix = copy.deepcopy(mat)
        if x < 0 or x >= GRID_SIZE + 1 or y < 1 or y >= GRID_SIZE:
            return None, -1, -1
        matrix[x][y], matrix[x][y - 1] = matrix[x][y - 1], matrix[x][y]
        return matrix, x, y - 1

    def position(self, matrix: List[List[int]]) -> tuple((int, int)):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if matrix[i][j] == 'B':
                    return (i, j)
    
    def find_blank(self, matrix: List[List[int]]) -> tuple((int, int)):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if matrix[i][j] == 'B':
                    return (i, j)
        return (-1, -1)


if __name__ == '__main__':
    g = Grid()
    matrix = g.target()
    g.display(matrix)
    g.display(g.top(matrix, 1, 1)[0])
    g.display(g.bottom(matrix, 1, 1)[0])
    g.display(g.right(matrix, 1, 1)[0])
    g.display(g.left(matrix, 1, 1)[0])
