import finProj as fp
from python.strategy.strategy import Strategy


class LongCallSpread(Strategy):
    def __init__(self, strikeA, strikeB, stock, timeToMaturity):
        """
        :param strikeA: strike for long call
        :param stirkeB: strike for short call
        :param stock: stock object that is the underlying
        :param timeToMaturity: time to maturity of all options

        assumes that strikeA < StrikeB
        """
        super().__init__(stock, timeToMaturity)
        self.strikeA = strikeA
        self.strikeB = strikeB

        self.options = []
        self.payoff = fp.Euro(fp.PayoffType.Call)

        self.options.append(fp.Option(self.stock, self.payoff, self.strikeA, self.timeToMaturity, fp.OptionPosition.Long))
        self.options.append(fp.Option(self.stock, self.payoff, self.strikeB, self.timeToMaturity, fp.OptionPosition.Short))

    def getMaxPayoff(self):
        return (self.strikeB - self.strikeA) - self.price()


