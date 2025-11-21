import finProj as fp
from python.strategy.longCallSpread import LongCallSpread

def main():
    """Main entry point of the program."""
    # p = fp.BinomialTree(1, 1/12.0, 0.05)
    p2 = fp.MonteCarlo(100000, 1/356.0, 0.05)
    # s = fp.Stock(p, 60, 0.30, 0.05)
    # pf = fp.EuroCall()
    # o = fp.Option(s, pf, 61, 1.0, fp.OptionPosition.Long)

    s2 = fp.Stock(p2, 60, 0.30, 0.05)
    lcs = LongCallSpread(61, 70, s2, 1)

    print(lcs.price())


if __name__ == "__main__":
    main()