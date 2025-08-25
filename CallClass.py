from scipy.stats import norm
import math
import numpy as np

class Call:
    def __init__(self, price, stirke, rf, sigma, short=False, start=0, end=1):
        self.price = price
        self.stirke = stirke
        self.risk_free = rf
        self.sigma = sigma
        self.short = short
        self.paths = None
        self.time = end-start
        self.start = start
        self.end = end

    def run(self, steps, strat, envt):
        # TODO: implement calculation
        # TODO: change how calc works with time, pass in time as a parameter
        self.paths = np.

        for i in range(0, steps):
            if i >= self.start and i < self.end:
                
        
    def calc_call(self):
        if self.time == 0:
            return self.calc_intrinsic()

        d1 = (np.log(self.price/self.stirke) + (self.risk_free+(np.pow(self.sigma, 2)/2))*self.time)/(self.sigma*np.sqrt(self.time))
        d2 = d1 - (self.sigma*np.sqrt(self.time))

        BSMpred = (self.price*norm.cdf(d1)) - (self.stirke*np.exp(-1*self.risk_free*self.time)*norm.cdf(d2))
        return BSMpred

    # returns the delta for a call and then a put in an array in that order
    def calc_delta(self):
        d1 = (math.log(self.price/self.stirke) + (self.risk_free+(math.pow(self.sigma, 2)/2))*self.time)/(self.sigma*math.sqrt(self.time))
        delta = norm.cdf(d1)
        return delta

    # use the norm.pdf function
    def calc_gamma(self):
        d1 = (math.log(self.price/self.stirke) + (self.risk_free+(math.pow(self.sigma, 2)/2))*self.time)/(self.sigma*math.sqrt(self.time))
        gamma = norm.pdf(d1)/(self.price*self.sigma*math.sqrt(self.time))
        return gamma

    def calc_vega(self):
        d1 = (math.log(self.price/self.stirke) + (self.risk_free+(math.pow(self.sigma, 2)/2))*self.time)/(self.sigma*math.sqrt(self.time))
        vega = self.price * norm.pdf(d1) * math.sqrt(self.time)
        return vega

    def calc_theta(self):
        d1 = (math.log(self.price/self.stirke) + (self.risk_free+(math.pow(self.sigma, 2)/2))*self.time)/(self.sigma*math.sqrt(self.time))
        d2 = d1 - (self.sigma*math.sqrt(self.time))

        secondCall = norm.cdf(d2)
        secondPut = norm.cdf(-1*d2)

        second = self.risk_free*self.stirke*math.exp(-1*self.risk_free*self.time)

        first = -1*(self.price*norm.pdf(d1)*self.sigma)/(2*math.sqrt(self.time))

        return first-(second*secondCall)

    def calc_rho(self):
        d1 = (math.log(self.price/self.stirke) + (self.risk_free+(math.pow(self.sigma, 2)/2))*self.time)/(self.sigma*math.sqrt(self.time))
        d2 = d1 - (self.sigma*math.sqrt(self.time))

        first = self.stirke*self.time*math.exp(-1*self.risk_free*self.time)

        return first*norm.cdf(d2)

    def calc_intrinsic(self):
        return max([self.price-self.stirke, 0])