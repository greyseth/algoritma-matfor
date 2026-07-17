def mat_subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def scalar_multiply(scalar, A):
    n = len(A)
    return [[scalar * A[i][j] for j in range(n)] for i in range(n)]

def determinant(A):
    n = len(A)
    
    # Base cases
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    # Recursive expansion along first row
    det = 0
    for col in range(n):
        # Build the submatrix excluding row 0 and current col
        submatrix = [
            [A[row][j] for j in range(n) if j != col]
            for row in range(1, n)
        ]
        sign = (-1) ** col
        det += sign * A[0][col] * determinant(submatrix)
    
    return det

def find_eigenvalues(AtA, I, candidates):
    """
    candidates: a list of lambda values to test
    returns those where det(AtA - lambda*I) is close to 0
    """
    eigenvalues = []
    
    for lam in candidates:
        scaled_I = scalar_multiply(lam, I)
        shifted = mat_subtract(AtA, scaled_I)
        det = determinant(shifted)
        
        if abs(det) < 0.001:  # close enough to zero
            eigenvalues.append(lam)
    
    # Sort in decreasing order
    eigenvalues.sort(reverse=True)
    return eigenvalues
