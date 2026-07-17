import math

from multiplication import *
from transpose import transposeMatrix
from gaussian import equation_system
from eigenvalue import find_eigenvalues
from magnitude import get_magnitude

matrix = [
  [3,2,1],
  [2,1,4]
]

AtA = multiply_matrix(transposeMatrix(matrix), matrix) # A transpos dikalikan dengan A

identity = [[1 if i == j else 0 for j in range(len(AtA))] for i in range(len(AtA))] # Matriks identitas

eigenvalues = find_eigenvalues(AtA, identity, list(range(0, 50))) # Mencari eigenvalue dari matriks A

# Mendapatkan Vt
Vt = []
for l in eigenvalues:
    identityLambda = list(map(lambda r: list(map(lambda d: l if d == 1 else 0, r)), identity))
    sub = subtract_matrices(AtA, identityLambda)

    homogenous = equation_system(sub, [0,0,0], circle_pivots=True,print_log=False).to_reduced_triangular()

    eigenvector = [0, 0, 1]
    for i, row in enumerate(homogenous.lhs):
        for j, d in enumerate(row):
            if d == 1.0:
                if j == 0: eigenvector[0] = row[j+2]
                else: eigenvector[1] = row[j+1]

    normalizedVector = scalar_multiply(eigenvector, 1/get_magnitude(eigenvector)) # matriks Vt
    Vt.append(normalizedVector) # Tidak perlu di transpos karena sudah sesuai bentuk

# Membuat matriks sigma
sigma = [[0 for _ in row] for row in matrix]
for index, v in enumerate(eigenvalues):
  if v == 0: continue
  sigma[index][index] = math.sqrt(eigenvalues[index])

# Membuat matriks U
U = []
for index, v in enumerate(eigenvalues):
    if v == 0: continue
    U.append(multiply_matrix_vector(scalar_multiply_2d(matrix, 1/math.sqrt(v)), Vt[index]))

result = multiply_matrix(multiply_matrix(U, sigma), Vt) # Hasil akhir

print("--Hasil Kompresi Menggunakan SVD--")
print('[')
for row in result:
  print(f"    {[val for val in row]},")
print(']')