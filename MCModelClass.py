from BSModelClass import BSModel
import numpy as np
import matplotlib.pyplot as plt
from rich.progress import track
import time

# assumes that 252 trading days in 1 years

class MCModel():
    def __init__(self):
        self.startPrice = 0
        self.vol = 0
        self.time = 0
        self.bsm = BSModel()
        pass

    def getInput(self, message, expected=None):
        if expected:
            while True:
                value = input(message).lower()
                if value in expected:
                    return value
                else:
                    print("Invalid Input")
        else:
            while True:
                value = input(message)
                try:
                    value = float(value)
                    return value
                except:
                    print("Invalid Format")

    def simulatePaths(self, drift, numPaths):
        N = int(self.time * 252)
        dt = float(1/252)
        
        Z = np.random.normal(size=(numPaths, N))

        lr = (drift - 0.5 * self.vol**2) * dt + self.vol * np.sqrt(dt) * Z

        S = self.startPrice * np.exp(np.cumsum(lr, axis=1))

        return S
    
    def run(self):
        pass

def getBestWorst(list, price):
    #indexs = np.linspace(0, list.shape[0]-1, list.shape[0]).reshape(list.shape[0], 1)
    lasts = list[:, -1]
    
    above = np.argwhere(lasts > price)
    atBelow = np.argwhere(lasts <= price)

    return above, atBelow
    
model = MCModel()

model.startPrice = 100
model.vol = 0.2
model.time = 1

strike = 100
r = 0.05
paths = 100
drift = 0.09

print("Calculating Stock Prices")
basket = model.simulatePaths(drift, paths)
new = np.full((basket.shape[0], 1), model.startPrice)
full = np.hstack((new, basket))
h, el = getBestWorst(full, model.startPrice)

avgHigh = np.sum(full[h], axis=0)/len(h)
avgLow = np.sum(full[el], axis=0)/len(el)

times = np.linspace(0, model.time, full.shape[1])
dte = model.time-times

for i in range(full.shape[0]):
    plt.plot(times, full[i], linewidth=0.8, alpha=0.5)

averagePrices = np.sum(full, axis=0)/paths
plt.plot(times, averagePrices, label = 'Average Price', color='b')
plt.plot(times, model.startPrice*np.ones(full.shape[1]), label= 'Start Price', color='k')
plt.plot(times, avgHigh[0], label='Average Above Price', color='g')
plt.plot(times, avgLow[0], label='Average Equal or Below Price', color='r')

plt.title('Sim Stock Price')
plt.legend(loc="upper left")
plt.show()

averagePrices = np.sum(full, axis=0)/paths

plt.plot(times, averagePrices)
plt.title('Average Stock Price')
plt.show()

dte = np.delete(dte, -1)
full = np.delete(full, -1, axis=1)

vecBSMCall = np.vectorize(model.bsm.calc_call)

for i in range(full.shape[0]):
    full[i] = vecBSMCall(full[i], strike, r, dte, model.vol)

for i in range(full.shape[0]):
    plt.plot(dte, full[i], linewidth=0.8)

plt.title('Sim Call Price')
plt.gca().invert_xaxis()

plt.show()

averagePrices = np.sum(full, axis=0)/paths

plt.plot(dte, averagePrices)
plt.title('Average Call Price')
plt.gca().invert_xaxis()
plt.show()

# # places to tkae this,
# # new graph with average, average profitable and un profitable paths, same for options
# # calculate average PnL for the options paths, better looking graphs