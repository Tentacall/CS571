from typing import List
import fileinput
import os
import copy
import random
import math
GRID_SIZE = 3

class Grid:

    def generate(self) -> List[List[int]]:
        # array = [i for i in range(1, GRID_SIZE**2)] + ['B']
        # random.shuffle(array)
        input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        array = []
        for line in fileinput.input(files=input_path):
            line = line.strip()
            line = line.split(' ')
            for num in line:
                array.append(int(num) if num != 'B' else num)
        matrix = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                row.append(array[i*GRID_SIZE + j])
            matrix.append(row)
        
        return matrix
    
    def find_blank(self, matrix: List[List[int]]) -> tuple((int, int)):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if matrix[i][j] == 'B':
                    return (i, j)
        return (-1, -1)
    
inpt = Grid()
matrix = inpt.generate()
posx, posy = inpt.find_blank(matrix)

def neighbour_function(l):
    return random.randint(0, l-1)

def cooling(t):
    return t*0.9999

def probability( fc, fn, T):
    return math.exp((fc-fn)/T)