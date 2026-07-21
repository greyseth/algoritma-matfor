import transpose
import numpy as np

def add(a, b):
    if (len(a.flatten()) != len(b.flatten()) or len(a) != len(b)):
        return print("Different matrix sizes")
    
    result = []
    
    for y, row in enumerate(a):
        resultRow = np.array([])
        for x, n in enumerate(row):
            resultRow = np.append(resultRow, n + b[y][x])
        
        result.append(resultRow)

    return np.array(result)

def subtract(a, b):
    if (len(a.flatten()) != len(b.flatten()) or len(a) != len(b)):
        return print("Different matrix sizes")
    
    result = []
    
    for y, row in enumerate(a):
        resultRow = np.array([])
        for x, n in enumerate(row):
            resultRow = np.append(resultRow, n - b[y][x])
        
        result.append(resultRow)

    return np.array(result)

def multiplication(a, _b):
    b = []
    
    if len(a) == len(_b) and len(a[0]) == len(_b[0]) and len(a) != len(a[0]):
        b = transpose.transposeMatrix(_b)
    else:
        b = _b

    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for y in range(len(a)):
        for x in range(len(b[0])):
            for k in range(len(b)):
                result[y][x] += a[y][k] * b[k][x]

    return np.array(result)

def power(matrix, amount):
    result = matrix

    for _ in range(amount - 1):
        result = multiplication(result, matrix)

    return result

inputA = np.array([
    [20, 15, 10],
    [18, 12, 14]
])

inputB = np.array([
    [12, 10, 8],
    [16, 11, 9]
])

inputC = np.array([
    [20, 15], [18, 12]
])

print(add(inputA, inputB))
print(subtract(inputA, inputB))
print(multiplication(inputA, inputB))

print(power(inputC, 2))