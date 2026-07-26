import numpy as np

criteria = ["Biaya", "Waktu", "Nyaman", "Aman", "Akses"]

# -- Matriks perbandingan berpasangan antar kriteria --
A = np.array([
    [1,    2,    2.5,  0.5,  2   ],   # Biaya
    [0.5,  1,    2,    0.33, 2   ],   # Waktu
    [0.4,  0.5,  1,    0.25, 0.5 ],   # Nyaman
    [2,    3,    4,    1,    3   ],   # Aman
    [0.5,  0.5,  2,    0.33, 1   ],   # Akses
])

n = A.shape[0]

print("Matriks perbandingan berpasangan:")
print(A)
print(f"Jumlah kriteria (n): {n}")

def compute_priority_vector(matrix):
    """
    Menghitung estimasi vektor eigen (bobot prioritas) dari matriks
    perbandingan berpasangan menggunakan metode normalisasi AHP.
    :param matrix: Matriks perbandingan berpasangan (n x n).
    :return: Jumlah kolom dan vektor prioritas (bobot ternormalisasi).
    """
    column_sums = matrix.sum(axis=0)
    normalized_matrix = matrix / column_sums
    priority_vector = normalized_matrix.mean(axis=1)
    return column_sums, normalized_matrix, priority_vector

column_sums, A_normalized, priority_vector = compute_priority_vector(A)

print("Jumlah tiap kolom:", column_sums)
print("\nMatriks ternormalisasi:")
print(np.round(A_normalized, 4))
print("\nVektor prioritas (estimasi vektor eigen):")
for c, p in zip(criteria, priority_vector):
    print(f"  {c:8s}: {p:.4f}")
print(f"Total bobot: {priority_vector.sum():.4f}")

def check_consistency(matrix, priority_vector, random_index=1.12):
    """
    Menghitung nilai eigen maksimum beserta rasio konsistensi (CR)
    dari matriks perbandingan berpasangan.
    :param matrix: Matriks perbandingan berpasangan (n x n).
    :param priority_vector: Vektor prioritas (estimasi vektor eigen).
    :param random_index: Random Index (RI) sesuai ukuran matriks.
    :return: lambda_max, CI, CR.
    """
    n = matrix.shape[0]

    # Ax menghasilkan estimasi lambda * x untuk tiap baris
    weighted_sum = matrix @ priority_vector
    lambda_estimates = weighted_sum / priority_vector
    lambda_max = lambda_estimates.mean()

    CI = (lambda_max - n) / (n - 1)
    CR = CI / random_index
    return lambda_max, CI, CR

lambda_max, CI, CR = check_consistency(A, priority_vector)

print(f"Nilai eigen maksimum (lambda_maks): {lambda_max:.4f}")
print(f"Consistency Index (CI): {CI:.4f}")
print(f"Consistency Ratio (CR): {CR:.4f}")

if CR <= 0.1:
    print("Kesimpulan: Matriks perbandingan KONSISTEN (CR <= 0.1), bobot prioritas dapat dipercaya.")
else:
    print("Kesimpulan: Matriks perbandingan TIDAK KONSISTEN (CR > 0.1), penilaian perlu ditinjau ulang.")