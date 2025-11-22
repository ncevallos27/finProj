import matplotlib.pyplot as plt
import numpy as np

class ViewStrategy:
    def __init__(self):
        pass

    def viewStrategyPayoff(self, strategy, bottomPrice, topPrice, deltaP=1):
        """
        plots all payoffs for a strategy
        :param strategy: strategy object
        :param bottomPrice: bottom price
        :param topPrice: top price
        :param deltaP: difference between prices
        :return: none
        """
        prices = np.arange(bottomPrice, topPrice + deltaP, deltaP)
        payoffs = [strategy.getPayoff(S) for S in prices]

        plt.figure(figsize=(8, 5))
        plt.plot(prices, payoffs)
        plt.xlabel("Stock Price (S)")
        plt.ylabel("Payoff")
        plt.title(f"Option Payoff Curve: {strategy}")
        plt.grid(True)
        plt.show()

    def viewStrategyPNL(self, strategy, bottomPrice, topPrice, strategyStart, deltaP=1):
        """
        plots all PNLs for a straegy
        :param strategy:
        :param bottomPrice:
        :param topPrice:
        :param strategyStart:
        :param deltaP:
        :return: None
        """
        prices = np.arange(bottomPrice, topPrice + deltaP, deltaP)
        payoffs = [(strategy.getPayoff(S)-strategyStart) for S in prices]

        plt.figure(figsize=(8, 5))
        plt.plot(prices, payoffs)
        plt.xlabel("Stock Price (S)")
        plt.ylabel("PNL")
        plt.title(f"Option PNL Curve: {strategy}")
        plt.grid(True)
        plt.show()

