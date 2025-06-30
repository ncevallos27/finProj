from scipy.stats import norm
import math

S = 100  #current stock price
K = 100  #strike price
r = 0.05  #risk free rate
T = 1  #time to expiration
sigma = 0.2  #volatility

class BSmodel():
    def __init__(self):
        pass

    def calc_call(price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        BSMpred = (price*norm.cdf(d1)) - (strike*math.exp(-1*rate*time)*norm.cdf(d2))
        return BSMpred

    def calc_put(price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        BSMpred = (strike*math.exp(-1*rate*time)*norm.cdf(-1*d2)) - (price*norm.cdf(-1*d1))
        return BSMpred

    # returns the delta for a call and then a put in an array in that order
    def calc_delta(price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        delta = norm.cdf(d1)
        return [delta, delta-1]

    # use the norm.pdf function
    def calc_gamma(price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        gamma = norm.pdf(d1)/(price*vol*math.sqrt(time))
        return gamma

    def calc_vega(price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        vega = price * norm.pdf(d1) * math.sqrt(time)
        return vega

    def calc_theta(price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        secondCall = norm.cdf(d2)
        secondPut = norm.cdf(-1*d2)

        second = rate*strike*math.exp(-1*rate*time)

        first = -1*(price*norm.pdf(d1)*vol)/(2*math.sqrt(time))

        return [first-(second*secondCall), first+(second*secondPut)]

    def calc_rho(price, strike, rate, time, vol):
        d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
        d2 = d1 - (vol*math.sqrt(time))

        first = strike*time*math.exp(-1*rate*time)

        return [first*norm.cdf(d2), -1*first*norm.cdf(-1*d2)]

    def calc_intrinsic(price, strike):
        return [max([price-strike, 0]), max([strike-price, 0])]