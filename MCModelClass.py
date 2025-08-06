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

    def simulatePaths(self, drift, numPaths, vol):
        N = int(self.time * 252)
        dt = float(1/252)
        
        Z = np.random.normal(size=(numPaths, N))

        lr = (drift - 0.5 * vol**2) * dt + vol * np.sqrt(dt) * Z

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

plt.ion()

model.startPrice = 100
model.vol = 0.2
model.time = 1

strike = 103
r = 0.05
paths = 100
drift = 0.02

days = int(model.time * 252)

vecEuropeCallPrice = np.vectorize(model.bsm.europeCallPrice)

# print("Calculating Stock Prices")
# basket = model.simulatePaths(drift, paths, model.vol)
# new = np.full((basket.shape[0], 1), model.startPrice)
# full = np.hstack((new, basket))
# h, el = getBestWorst(full, model.startPrice)

# avgHigh = np.sum(full[h], axis=0)/len(h)
# avgLow = np.sum(full[el], axis=0)/len(el)

times = np.linspace(0, model.time, days+1)
dte = model.time-times

# sfig, saxes = plt.subplots(2, figsize=(10, 8))

# for i in range(full.shape[0]):
#     saxes[0].plot(times, full[i], linewidth=0.8, alpha=0.5)

# averagePrices = np.sum(full, axis=0)/paths
# saxes[0].plot(times, averagePrices, label = 'Average Price', color='b')
# saxes[0].plot(times, model.startPrice*np.ones(full.shape[1]), label= 'Start Price', color='k')
# saxes[0].plot(times, avgHigh[0], label='Average Above Price', color='g')
# saxes[0].plot(times, avgLow[0], label='Average Equal or Below Price', color='r')

# saxes[0].set_title('Sim Stock Price')
# saxes[0].legend(loc="upper left")

# averagePrices = np.sum(full, axis=0)/paths

# saxes[1].plot(times, averagePrices)
# saxes[1].set_title('Average Stock Price')

# sfig.suptitle("Stock Calculations")
# plt.show()
# plt.pause(0.01)

# # OPTIONS CODE FOR STOCK

# options = np.empty((full.shape[0], full.shape[1]))

# for i in range(full.shape[0]):
#     options[i] = vecEuropeCallPrice(full[i], strike, r, dte, model.vol)

# startPrice = options[:, 0]

# fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# for i in range(options.shape[0]):
#     axes[0, 0].plot(dte, options[i], linewidth=0.8, alpha = 0.40)

# h, el = getBestWorst(options, startPrice[0])

# avgHigh = np.sum(options[h], axis=0)/len(h)
# avgLow = np.sum(options[el], axis=0)/len(el)

# averagePrices = np.sum(options, axis=0)/paths

# axes[0, 0].plot(dte, averagePrices, label = 'Average Price', color='b')
# axes[0, 0].plot(dte, startPrice[0]*np.ones(options.shape[1]), label= 'Start Price', color='k')
# axes[0, 0].plot(dte, avgHigh[0], label='Average Above Price', color='g')
# axes[0, 0].plot(dte, avgLow[0], label='Average Equal or Below Price', color='r')

# axes[0, 0].set_title('Sim Call Price')
# axes[0, 0].invert_xaxis()
# axes[0, 0].legend(loc="upper left")

# axes[0, 1].plot(dte, averagePrices)
# axes[0, 1].set_title('Average Call Price')
# axes[0, 1].invert_xaxis()

# pnl = options-startPrice[:, np.newaxis]

# for i in range(pnl.shape[0]):
#     postive = pnl[i] > 0
#     negative = pnl[i] < 0
#     axes[1, 0].plot(dte, pnl[i], linewidth=0.8, alpha=0.05, color='k')
#     axes[1, 0].fill_between(dte, pnl[i], 0, where=postive, color='g', alpha=0.02)
#     axes[1, 0].fill_between(dte, pnl[i], 0, where=negative, color='r', alpha=0.02)

# axes[1, 0].set_title('PnL For Call')
# axes[1, 0].invert_xaxis()

# averagePnl = np.sum(pnl, axis=0)/paths
# postive = averagePnl > 0
# negative = averagePnl < 0

# axes[1, 1].plot(dte, averagePnl, linewidth=0.8, color='k')
# axes[1, 1].fill_between(dte, averagePnl, 0, where=postive, color='g', alpha=0.1)
# axes[1, 1].fill_between(dte, averagePnl, 0, where=negative, color='r', alpha=0.1)
# axes[1, 1].set_title('Average pnl')
# axes[1, 1].invert_xaxis()

# fig.suptitle("Options Calculations")

# plt.show()
# plt.pause(0.01)

# input("Part 1 complete. Press Enter to close plots...")

# # places to tkae this,
# # new graph with average, average profitable and un profitable paths, same for options
# # calculate average PnL for the options paths, better looking graphs

numPerVol = 100
startVol = 0.1
endVol = 0.5
numVols = 20

totalPath = numPerVol*numVols

volfig, volAxes = plt.subplots(2, figsize=(10, 8))
ovolfig, ovolAxes = plt.subplots(2, figsize=(10, 8))
pnlfig, pnlAxes = plt.subplots(2, figsize=(10, 8))

vols = np.linspace(startVol, endVol, numVols)

cmap = plt.get_cmap('inferno')
colors = [cmap(i) for i in np.linspace(0, 1, numVols)]

prices = np.empty((0, days+1))
optionsPrices = np.empty((0, days+1))

times = np.linspace(0, model.time, prices.shape[1])

for i, vol in enumerate(vols):
    basket = model.simulatePaths(drift, numPerVol, vol)
    new = np.full((basket.shape[0], 1), model.startPrice)
    full = np.hstack((new, basket))
    options = np.empty((full.shape[0], days+1))
    for j in range(full.shape[0]):
        options[j] = vecEuropeCallPrice(full[j], strike, r, dte, vol)
        if j == 0:
            volAxes[0].plot(times, full[j], label=f"vol: {round(vol, 4)}", color=colors[i], alpha=0.1)
            ovolAxes[0].plot(times, options[j], label=f"vol: {round(vol, 4)}", color=colors[i], alpha=0.1)
        else:
            if j < 50:
                volAxes[0].plot(times, full[j], color=colors[i], alpha=0.1)
                ovolAxes[0].plot(times, options[j], color=colors[i], alpha=0.1)

    prices = np.vstack((prices, full))
    optionsPrices = np.vstack((optionsPrices, options))
    

volAxes[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
volAxes[0].set_title("Prices")

ovolAxes[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
ovolAxes[0].set_title("Options Prices")

# print(optionsPrices.shape)
# print(prices.shape)

avgprices = np.empty((0, days+1))
avgoprices = np.empty((0, days+1))

for i, vol in enumerate(vols):
    full = prices[i*numPerVol:(i+1)*numPerVol]
    fullOptions = optionsPrices[i*numPerVol:(i+1)*numPerVol]

    avgprices = np.vstack((avgprices, full))
    avgoprices = np.vstack((avgoprices, fullOptions))

    averageBasket = np.sum(full, axis=0)/numPerVol
    averageOptionBasket = np.sum(fullOptions, axis=0)/numPerVol

    volAxes[1].plot(times, averageBasket, label=f"vol: {round(vol, 4)}", color=colors[i])
    ovolAxes[1].plot(times, averageOptionBasket, label=f"vol: {round(vol, 4)}", color=colors[i])

volAxes[1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
volAxes[1].set_title("Averages")

ovolAxes[1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
ovolAxes[1].set_title("Averages")

volfig.tight_layout()
ovolfig.tight_layout()
plt.show()

plt.pause(0.01)
input("Simulation complete. Press Enter to close plots...")

plt.close()