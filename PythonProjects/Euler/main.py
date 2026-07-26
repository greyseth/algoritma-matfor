import numpy as np

def solve_underdamped_rlc(R, L, C, I0, dI0, t):
    """
    Menyelesaikan arus I(t) pada rangkaian RLC seri tanpa sumber
    untuk kasus underdamped, menggunakan Rumus Euler untuk mengubah
    solusi akar kompleks konjugat menjadi bentuk osilasi teredam real.
    :param R: Resistansi (Ohm).
    :param L: Induktansi (Henry).
    :param C: Kapasitansi (Farad).
    :param I0: Arus awal, I(0).
    :param dI0: Turunan arus awal, dI/dt pada t=0.
    :param t: Array waktu.
    :return: alpha, omega_d, dan array arus I(t).
    """
    # -- Koefisien persamaan karakteristik s^2 + (R/L)s + 1/(LC) = 0 --
    a_koef = R / L
    b_koef = 1 / (L * C)

    diskriminan = a_koef**2 - 4 * b_koef
    if diskriminan >= 0:
        raise ValueError("Rangkaian tidak underdamped (diskriminan >= 0)")

    alpha = R / (2 * L)                       # koefisien redaman
    omega_d = np.sqrt(b_koef - alpha**2)       # frekuensi osilasi teredam

    # -- Akar kompleks konjugat: s = -alpha +/- j*omega_d --
    # Solusi umum I(t) = A1*e^(s1*t) + A2*e^(s2*t)
    # Dengan Rumus Euler, disederhanakan menjadi:
    # I(t) = e^(-alpha*t) * (B1*cos(omega_d*t) + B2*sin(omega_d*t))

    # -- Menentukan B1, B2 dari kondisi awal --
    B1 = I0
    B2 = (dI0 + alpha * B1) / omega_d

    I_t = np.exp(-alpha * t) * (B1 * np.cos(omega_d * t) + B2 * np.sin(omega_d * t))
    return alpha, omega_d, I_t


# -- Parameter rangkaian RLC (dipilih agar underdamped) --
R, L, C = 20.0, 0.5, 1e-3   # Ohm, Henry, Farad
I0, dI0 = 2.0, 0.0          # kondisi awal arus

t = np.linspace(0, 0.3, 500)
alpha, omega_d, I_t = solve_underdamped_rlc(R, L, C, I0, dI0, t)

print(f"Koefisien redaman (alpha)     : {alpha:.4f}")
print(f"Frekuensi osilasi teredam (omega_d): {omega_d:.4f} rad/s")
print(f"I(0) = {I_t[0]:.4f} A (seharusnya = {I0} A)")