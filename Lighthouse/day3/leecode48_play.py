from typing import List

import os
import time

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix[i].reverse()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"[{item}]" for item in row))

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,1],[2,3,2],[1,2,1]]
matrix2 = [[2,1,2],[1,3,1],[2,1,2]]

# matrix = [['#'] * 3 for _ in range(3)]
while True:
    clear_screen()
    print_matrix(matrix)
    # rotate(matrix)
    time.sleep(0.2)
    
    clear_screen()
    print_matrix(matrix2)
    time.sleep(0.2)