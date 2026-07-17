import pandas as pd

def parseData(filename, importColumns, xRowName, yRowName, nrows, skipRows=0):
    df = pd.read_excel(filename, usecols=importColumns, skiprows=skipRows, nrows=nrows)

    xRow = df[xRowName].to_numpy()
    yRow = df[yRowName].to_numpy()

    if (len(xRow) != len(yRow)):
        print("Failed to parse data: length of X and Y do not match")
        return None
    
    return (xRow, yRow)