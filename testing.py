import finProj as fp
from python.strategy.longCallSpread import LongCallSpread
from python.display.viewStock import ViewStock
from python.display.viewOption import ViewOption
from python.display.viewStrategy import ViewStrategy

def main():
    """Main entry point of the program."""
    # p = fp.BinomialTree(1, 1/12.0, 0.05)
    p2 = fp.MonteCarlo(100000, 1/356.0, 0.05)
    # s = fp.Stock(p, 60, 0.30, 0.05)
    # pf = fp.EuroCall()-
    # o = fp.Option(s, pf, 61, 1.0, fp.OptionPosition.Long)

    s2 = fp.Stock(p2, 60, 0.30, 0.05)
    pf2 = fp.Asian(fp.PayoffType.Call, 30)
    o2 = fp.Option(s2, pf2, 61, 1.0, fp.OptionPosition.Long)
    lcs = LongCallSpread(61, 70, s2, 1)

    # o2.price()
    # # viewer = ViewStock()
    # # # viewer.plotStockPaths(s2)
    # # viewerOption = ViewOption()
    # # viewerOption.plotOptionPayoff(o2, 55, 75, 0.5)
    # # viewerOption.plotOptionPNL(o2, 55, 75, o2.price(), 0.5)
    #
    # viewerStrategy = ViewStrategy()
    #
    # viewerStrategy.viewStrategyPayoff(lcs, 55, 75, 0.5)
    # viewerStrategy.viewStrategyPNL(lcs, 55, 75, lcs.price(), 0.5)



if __name__ == "__main__":
    main()