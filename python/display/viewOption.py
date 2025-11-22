import matplotlib.pyplot as plt
import numpy as np


class ViewOption:
    def __init__(self):
        pass

    def plotOptionPayoff(self, option, bottomPrice, topPrice, deltaP=1):
        """
        :param option: the option to view
        :param bottomPrice: the bottom of the price range to plot
        :param topPrice: the top of the price range to plot (inclusive)
        :param deltaP: the change in price step
        :return: no return value

        plots all payoffs for option
        """
        prices = np.arange(bottomPrice, topPrice + deltaP, deltaP)
        payoffs = [option.fakeCalculate(S, option.getStrike()) for S in prices]

        plt.figure(figsize=(8, 5))
        plt.plot(prices, payoffs)
        plt.xlabel("Stock Price (S)")
        plt.ylabel("Payoff")
        plt.title(f"Option Payoff Curve: {option}")
        plt.grid(True)
        plt.show()

    def plotOptionPNL(self, option, bottomPrice, topPrice, optionStart, deltaP=1):
        """
        plots the PNL of the option over the range of values
        :param option: option object
        :param bottomPrice: bottom price for plot
        :param topPrice: top price for plot
        :param optionStart: the price of the option at the start
        :param deltaP: steps betweem the prices
        :return: none
        """
        prices = np.arange(bottomPrice, topPrice + deltaP, deltaP)
        payoffs = [(option.fakeCalculate(S, option.getStrike())-optionStart) for S in prices]

        plt.figure(figsize=(8, 5))
        plt.plot(prices, payoffs)
        plt.xlabel("Stock Price (S)")
        plt.ylabel("Payoff")
        plt.title(f"Option PNL Curve: {option}")
        plt.grid(True)
        plt.show()


