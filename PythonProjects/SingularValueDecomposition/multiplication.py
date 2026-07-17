def scalar_multiply(A, S):
    return [d*S for d in A]

def scalar_multiply_2d(A, S):
    return [[d*S for d in row] for row in A]

def multiply_matrix(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError(f"Incompatible shapes: ({rows_A}x{cols_A}) @ ({rows_B}x{cols_B})")

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def multiply_matrix_vector(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix columns must match vector length.")
    
    result = []
    
    for row in matrix:
        # Calculate the dot product for the current row
        row_total = 0
        for i in range(len(vector)):
            row_total += row[i] * vector[i]
        
        result.append(row_total)
        
    return result

def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    
    if len(B) != rows or len(B[0]) != cols:
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    result = [
        [A[i][j] - B[i][j] for j in range(cols)]
        for i in range(rows)
    ]
    
    return result