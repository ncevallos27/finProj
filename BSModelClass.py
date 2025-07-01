from scipy.stats import norm
import math
import numpy as np

S = 100  #current stock price
K = 100  #strike price
r = 0.05  #risk free rate
T = 1  #time to expiration
sigma = 0.2  #volatility

class BSModel():
    def __init__(self):
        pass

    def run(self):
        print("\nRunning Black Scholes Model")
        print("Select An Option Below")
        print("1. Calculate")
        print("2. Grid Calculator")
        #print("3. See Usage")
        #print("4. See Info")
        print("5. Quit")

        while True:
            selected = 0
            while True:
                selected = input("Number: ")
                try:
                    selected = int(selected)
                    break
                except:
                    print("Invalid Input")

            if selected == 1:
                self.calculate()
                break
            elif selected == 2:
                self.gridCalc()
                break
            elif selected == 5:
                return 1
            else:
                print("Not an Option")

        return 0

    def usage(self):
        pass

    def info(self):
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

    def calculate(self):
        print("\nCalculator")
        stockPrice = self.getInput("Enter Stock Price: ")
        strikePrice = self.getInput("Enter Strike Price: ")
        rfrate = self.getInput("Enter Risk Free Rate as a decimal: ")
        time = self.getInput("Enter Time in Years: ")
        vol = self.getInput("Enter Volatility: ")

        print(f"\nEntered Paramaters: {stockPrice}, {strikePrice}, {rfrate}, {time}, {vol}")

        print("\n type:   CALL   PUT")
        print(f"price:   {round(self.calc_call(stockPrice, strikePrice, rfrate, time, vol), 2)}   {round(self.calc_put(stockPrice, strikePrice, rfrate, time, vol), 2)}")
        deltas = self.calc_delta(stockPrice, strikePrice, rfrate, time, vol)
        gamma = self.calc_gamma(stockPrice, strikePrice, rfrate, time, vol)
        vega = self.calc_vega(stockPrice, strikePrice, rfrate, time, vol)
        thetas = self.calc_theta(stockPrice, strikePrice, rfrate, time, vol)
        rhos = self.calc_rho(stockPrice, strikePrice, rfrate, time, vol)
        intrinsics = self.calc_intrinsic(stockPrice, strikePrice)
        print(f"deltas:   {round(deltas[0], 3)}   {round(deltas[1], 3)}")
        print(f"gamma:   ---({round(gamma, 5)})---")
        print(f"vega:   ---({round(vega, 3)})---")
        print(f"thetas:   {round(thetas[0], 3)}   {round(thetas[1], 3)}")
        print(f"rhos:   {round(rhos[0], 3)}   {round(rhos[1], 3)}")
        print(f"intrinsics:   {round(intrinsics[0], 2)}   {round(intrinsics[1], 2)}")

    def gridCalc(self):
        print("\nGrid Calculator")
        
        minstockPrice = self.getInput("Enter Min Stock Price: ")
        maxstockPrice = self.getInput("Enter Max Stock Price: ")
        strikePrice = self.getInput("Enter Strike Price: ")
        rfrate = self.getInput("Enter Risk Free Rate as a decimal: ")
        time = self.getInput("Enter Time in Years: ")
        minVol = self.getInput("Enter Min Volatility: ")
        maxVol = self.getInput("Enter Max Volatility: ")

        stockPrices = np.linspace(minstockPrice, maxstockPrice, 10)
        volValues = np.linspace(minVol, maxVol, 10)

        optionType = self.getInput("Enter type of option 'c' for call or 'p' for put: [c/p] ", ['c', 'p'])
        
        print(f'{"".rjust(6)} ', end="")
        for vol in volValues:
            print(f'{str(round(vol, 3)).rjust(6)} ', end="")
        print("")

        for price in stockPrices:
            print(f'{str(round(price, 2)).rjust(6)} ', end="")
            for volVal in volValues:
                if optionType == 'c':
                    print(f'{str(round(self.calc_call(price, strikePrice, rfrate, time, volVal), 2)).rjust(6)} ', end="")
                else:
                    print(f'{str(round(self.calc_put(price, strikePrice, rfrate, time, volVal), 2)).rjust(6)} ', end="")
                
            print("")


    def calc_call(self, price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        BSMpred = (price*norm.cdf(d1)) - (strike*math.exp(-1*rate*time)*norm.cdf(d2))
        return BSMpred

    def calc_put(self, price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        BSMpred = (strike*math.exp(-1*rate*time)*norm.cdf(-1*d2)) - (price*norm.cdf(-1*d1))
        return BSMpred

    # returns the delta for a call and then a put in an array in that order
    def calc_delta(self, price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        delta = norm.cdf(d1)
        return [delta, delta-1]

    # use the norm.pdf function
    def calc_gamma(self, price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        gamma = norm.pdf(d1)/(price*vol*math.sqrt(time))
        return gamma

    def calc_vega(self, price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        vega = price * norm.pdf(d1) * math.sqrt(time)
        return vega

    def calc_theta(self, price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        secondCall = norm.cdf(d2)
        secondPut = norm.cdf(-1*d2)

        second = rate*strike*math.exp(-1*rate*time)

        first = -1*(price*norm.pdf(d1)*vol)/(2*math.sqrt(time))

        return [first-(second*secondCall), first+(second*secondPut)]

    def calc_rho(self, price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        first = strike*time*math.exp(-1*rate*time)

        return [first*norm.cdf(d2), -1*first*norm.cdf(-1*d2)]

    def calc_intrinsic(self, price, strike):
        return [max([price-strike, 0]), max([strike-price, 0])]