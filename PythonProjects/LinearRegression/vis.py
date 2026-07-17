import matplotlib.pyplot as plt

def generateDiagram(data, regression):
    plt.figure(figsize=(8, 5))
    plt.scatter(data[0], data[1], color='royalblue', alpha=0.7, label="Points")
    plt.axline(xy1=(0, regression[0]), slope=regression[1])

    plt.title("Linear Regression Diagram", fontsize=14, pad=15)
    plt.xlabel("Benchmark Komputer (X)", fontsize=11)
    plt.ylabel("Jam Penggunaan (Y)", fontsize=11)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.show()