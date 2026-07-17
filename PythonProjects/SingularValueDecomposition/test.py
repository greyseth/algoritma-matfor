import math

def create_sigma(matrix, eigenvalues):
    newMatrix = [[0 for _ in row] for row in matrix]
    for index, v in enumerate(eigenvalues):
        if v == 0: continue
        newMatrix[index][index] = math.sqrt(eigenvalues[index])
    return newMatrix