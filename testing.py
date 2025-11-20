import finProj as fp
def main():
    """Main entry point of the program."""
    p = fp.BinomialTree(1, 1/8.0, 0.04)
    s = fp.Stock(p, 52, 0.28)
    pf = fp.EuroCall()
    o = fp.Option(s, pf, 50, 0.5, fp.OptionPosition.Long)

    print(o.price())



if __name__ == "__main__":
    main()