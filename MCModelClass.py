from BSModelClass import BSModel
import numpy as np
import matplotlib.pyplot as plt

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

        lr = (drift - (0.5 * (self.vol**2))) * dt + (drift * np.sqrt(dt) * Z)

        S = self.startPrice * np.exp(np.cumsum(lr, axis=1))

        return S
    
    def run(self):
        pass

model = MCModel()

model.startPrice = 100
model.vol = 0.2
model.time = 1

strike = 100
r = 0.05

basket = model.simulatePaths(0.08, 100)
full = np.insert(basket, 0, model.startPrice*np.ones((basket.shape[0], 1)), axis=0)

time = np.linspace(0, model.time, full.shape[1])
dte = model.time-time
print(dte)

for i in range(full.shape[0]):
    plt.plot(time, full[i], linewidth=0.8)

plt.show()

dte = np.delete(dte, -1)
print(dte)
full = np.delete(full, -1, axis=1)

vecBSMCall = np.vectorize(model.bsm.calc_call)
for i in range(full.shape[0]):
    full[i] = vecBSMCall(full[i], strike, r, dte, model.vol)

for i in range(full.shape[0]):
    plt.plot(dte, full[i], linewidth=0.8)

plt.gca().invert_xaxis()

plt.show()

# places to tkae this,
# new graph with average, average profitable and un profitable paths, same for options
# calculate average PnL for the options paths, better looking graphs