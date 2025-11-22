import matplotlib.pyplot as plt


class ViewStock:
    def __init__(self):
        pass

    def plotStockPaths(self, stock):
        """
        stock: a C++ Stock object exposed to Python via pybind11
        with method getRefPrices() returning list[list[float]]
        """
        paths = stock.getRefPrices()

        for path in paths:
            steps = range(len(path))
            plt.plot(steps, path)

        plt.xlabel("Step")
        plt.ylabel("Price")
        plt.title("Simulated Stock Paths")
        plt.grid(True)
        plt.show()
