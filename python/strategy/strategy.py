import finProj as fp

class Strategy:
    def __init__(self):
        self.options = []

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
