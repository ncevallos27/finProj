import finProj as fp
def main():
    """Main entry point of the program."""
    p = fp.BinomialTree(1, 1/8.0, 0.04)
    p2 = fp.MonteCarlo(1000, 1/356.0, 0.05)
    s = fp.Stock(p2, 60, 0.30, 0.05)
    pf = fp.EuroCall()
    o = fp.Option(s, pf, 61, 1.0, fp.OptionPosition.Long)

    print(o.price())


if __name__ == "__main__":
    main()