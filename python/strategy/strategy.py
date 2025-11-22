import finProj as fp
import numpy as np

class Strategy:
    def __init__(self, stock, timeToMaturity):
        self.options = []
        self.stock = stock
        self.timeToMaturity = timeToMaturity

    def price(self, step=None):
        totalCost = 0
        for option in self.options:
            if step:
                price = option.price(step)
            else:
                price = option.price()

            # print(price)
            if option.getPosition() == fp.OptionPosition.Long:
                totalCost += price
            else:
                totalCost -= price

        return totalCost

    def getPayoff(self, priceEnd):
        totalPayoff = 0
        for option in self.options:
            price = option.fakeCalculate(priceEnd, option.getStrike())
            # print(price)
            if option.getPosition() == fp.OptionPosition.Long:
                totalPayoff += price
            else:
                totalPayoff -= price

        return totalPayoff

    # TODO: need to implement
    # def generatePriceVector(self):
    #     """
    #     :return: generates all the prices for this strategy over its entire life
    #     """
    #     totalExpectation = 0
    #     timeStep = self.stock.getPricerTimeStep()
    #     for option in self.options:
    #         price = option.getExpectation(option.getMaturity())
    #         # print(price)
    #         if option.getPosition() == fp.OptionPosition.Long:
    #             totalExpectation += price
    #         else:
    #             totalExpectation -= price
    #
    #     times = np.arange(0, self.timeToMaturity + timeStep, timeStep)
    #     return [totalExpectation * self.stock.getDiscount(S) for S in reversed(times)]



