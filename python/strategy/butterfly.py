import finProj as fp
from python.strategy.strategy import Strategy


class ButterflyStrategy(Strategy):
    def __init__(self, stock, strikeA, strikeB, timeToMaturity):
        """
        defines a butterfly streategy
        :param stock: stock object
        :param strikeA: strike for bottom call
        :param strikeB: strike for top call
        :param timeToMaturity: total maturity
        """
        super().__init__(stock, timeToMaturity)
        self.strikeA = strikeA
        self.strikeB = strikeB

        self.payoff = fp.Euro(fp.PayoffType.Call)

        self.options.append(fp.Option(self.stock, self.payoff, self.strikeA, self.timeToMaturity, fp.OptionPosition.Long))
        self.options.append(fp.Option(self.stock, self.payoff, self.stock.getStart(), self.timeToMaturity, fp.OptionPosition.Short))
        self.options.append(fp.Option(self.stock, self.payoff, self.stock.getStart(), self.timeToMaturity, fp.OptionPosition.Short))
        self.options.append(fp.Option(self.stock, self.payoff, self.strikeB, self.timeToMaturity, fp.OptionPosition.Long))
