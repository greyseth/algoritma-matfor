import numpy as np
from scipy.sparse import csr_matrix
import time
from scipy.sparse import random

def page_rank_without_iteration(adjacency_matrix):
    """
    Computes the PageRank using the eigenvector method.
    :param adjacency_matrix: Sparse adjacency matrix (numpy array or scipy.sparse.csr_matrix).
    :return: PageRank vector and computation time.
    """

    column_sums = np.array(adjacency_matrix.sum(axis=0)).flatten()
    column_sums[column_sums == 0] = 1  # Avoid division by zero

    diagonal_scaling = csr_matrix((1 / column_sums, (np.arange(len(column_sums)), np.arange(len(column_sums)))), shape=(len(column_sums), len(column_sums)))
    
    transition_matrix = adjacency_matrix @ diagonal_scaling

    if not isinstance(transition_matrix, csr_matrix):
        transition_matrix = csr_matrix(transition_matrix)

    # Start timer
    start_time = time.time()

    # Compute PageRank
    eigenvalues, eigenvectors = np.linalg.eig(transition_matrix.toarray())
    eigenvalue_index = np.argmax(eigenvalues)
    rank_vector = np.abs(eigenvectors[:, eigenvalue_index])
    rank_vector /= rank_vector.sum()  # Normalize

    # End timer
    end_time = time.time()
    computation_time = end_time - start_time

    return rank_vector, computation_time

def page_rank(adjacency_matrix, damping_factor=0.85, max_iter=100, tol=1e-6):
    """
    Computes the PageRank using the power iteration method.
    :param adjacency_matrix: Sparse adjacency matrix (numpy array or scipy.sparse.csr_matrix).
    :param damping_factor: Probability of following a link (default 0.85).
    :param max_iter: Maximum number of iterations.
    :param tol: Convergence tolerance.
    :return: PageRank vector and computation time.
    """
    n = adjacency_matrix.shape[0]

    column_sums = np.array(adjacency_matrix.sum(axis=0)).flatten()
    column_sums[column_sums == 0] = 1  # Avoid division by zero

    # Create a diagonal matrix with the reciprocal of column sums
    diagonal_scaling = csr_matrix((1 / column_sums, (np.arange(len(column_sums)), np.arange(len(column_sums)))), shape=(len(column_sums), len(column_sums)))

    # Normalize adjacency matrix columns
    transition_matrix = adjacency_matrix @ diagonal_scaling  # Efficient sparse matrix multiplication

    # Convert to a sparse format if not already sparse
    if not isinstance(transition_matrix, csr_matrix):
        transition_matrix = csr_matrix(transition_matrix)
    
    # Initialize rank vector
    rank_vector = np.ones(n) / n

    # Start timer
    start_time = time.time()

    # iteration
    for iteration in range(max_iter):
        new_rank_vector = damping_factor * transition_matrix.dot(rank_vector) + (1 - damping_factor) / n
        if np.linalg.norm(new_rank_vector - rank_vector, ord=1) < tol:
            print(f"Converged after {iteration + 1} iterations.")
            break
        rank_vector = new_rank_vector

    # End timer
    end_time = time.time()
    computation_time = end_time - start_time

    return rank_vector, computation_time

def make_adjacency_matrix(n_pages, density):
    """
    Creates a random adjacency matrix.
    :param n: Number of nodes.
    :param p: Probability of an edge between two nodes.
    :return: Sparse adjacency matrix (numpy array or scipy.sparse.csr_matrix).
    """

    # Random untuk testing
    adjacency_matrix = random(n_pages, n_pages, density=density, format='csr', random_state=42, data_rvs=np.ones)
    np.fill_diagonal(adjacency_matrix.toarray(), 0)  # Remove self-links
    # Konversi elemen menjadi bilangan bulat (0 atau 1)
    adjacency_matrix.data = (adjacency_matrix.data > 0).astype(int)

    # End timer
    end_time = time.time()
    print("Adjacency matrix created.")
    print(f"Matrix size: {n_pages}x{n_pages}")
    print(f"Density: {density}")
    print(f"Matrix creation time: {end_time - start_time:.6f} seconds.")
    return adjacency_matrix

if __name__ == "__main__":
    print("Starting make adjacency matrix...")

    # Start timer
    start_time = time.time()

    adjacency_matrix = make_adjacency_matrix(10000, 0.001)
    # adjacency_matrix = [
    #     [0, 0, 1, 1],
    #     [1, 0, 0, 0],
    #     [1, 1, 0, 1],
    #     [1, 1, 0, 0]
    # ]
    # adjacency_matrix = np.array(adjacency_matrix, dtype=float)
    # print("Adjacency matrix:")
    # print(adjacency_matrix)
    print("")
    # Compute
    print("Starting PageRank computation...")
    rank_vector, computation_time = page_rank(adjacency_matrix)
    print("PageRank computation completed.")
    print(f"Computation time: {computation_time:.9f} seconds.")
    print("Top 10 PageRanks:", np.argsort(-rank_vector)[:10])