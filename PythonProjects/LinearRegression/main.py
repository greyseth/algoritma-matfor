import excelParse as parse
import regression as regression
import vis as vis

data = parse.parseData(
    'dataset.xlsx', 
    'F:G', 
    'Total Benchmark', 
    'Rata rata jam penggunaan laptop per hari', 
    47) # (x, y)
if (data != None):
    # outputs data in table view
    print('Parsed Data:')
    for i in range(len(data[0])):
        print(f"| {data[0][i]:,} | {data[1][i]:,} |")

    print("Is this data correct? (y/n)")
    if (str(input()).lower() == 'y'):
        # calcultes the regression
        regResult = regression.countRegression(data[0], data[1]) # (a, b)
        print(f"Regression result: y = {round(regResult[0], 3):,} + {regResult[1]:3g}X")

        # create diagram
        print("Display regression diagram? (y/n)")
        if (str(input()).lower() == 'y'):
            vis.generateDiagram(data, regResult)