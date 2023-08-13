from typing import List
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
        for row in matrix:
            for v in row:
                print(f"{v} ", end="")
            print()

    def target(self) -> List[List[int]]:
        return [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]


if __name__ == '__main__':
    g = Grid()
    g.display(g.target())
