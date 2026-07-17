import math
import numpy as np

# Input is in the form of an array
def dft(x):
    result = []

    for k in range(len(x)):
        realNum = 0
        imaginaryNum = 0

        # Sigma
        for n in range(len(x)):
            # Perhitungan euler

            angle = 2 * math.pi * k * n / len(x) # 2pi*k*n/N
            realNum += x[n] * math.cos(angle) # Xn * e
            imaginaryNum -= x[n] * math.sin(angle) # Xn * e

        result.append((realNum, imaginaryNum))

    return result

def fft(x):
    N = len(x)
    
    if (N % 2 > 0): raise ValueError("length of x must be a power of 2")
    elif (N <= 32): return dft(x)
    else:
        xEven = fft(x[::2])
        xOdd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([xEven + factor[:N / 2] * xOdd,
                               xEven + factor[N / 2:] * xOdd])

input = [1, 2, 3, 4]
print(fft(input))