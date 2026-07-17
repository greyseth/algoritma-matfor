def countAverage(array):
    sum = 0
    for num in array:
        sum += num
    
    return sum / len(array)

def countRegression(x, y):
    xAvg = countAverage(x)
    yAvg = countAverage(y)

    # b value
    sigmaTop = 0
    sigmaBottom = 0

    for i in range(len(x)):
        sigmaTop += (x[i] - xAvg) * (y[i] - yAvg)
        sigmaBottom += (x[i] - xAvg)**2
    
    b = sigmaTop / sigmaBottom

    # a value
    a = yAvg - b*xAvg

    return (a, b)