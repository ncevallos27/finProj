from BSModelClass import BSModel

class App():
    def __init__(self, m=None):
        model = m

    def setModel(self):
        print("\nSelect Model")
        print("1. Black Scholes Model")
        while True:
            selected = 0
            while True:
                selected = input("Number: ")
                try:
                    selected = int(selected)
                    break
                except:
                    print("Invalid Input")

            if selected == 1:
                self.model = BSModel()
                break
            else:
                print("Invalid Input Try Again")

    def run(self):
        print("\nSelect Option Below")
        print("1. Run Option Pricing")
        print("2. Search Ticker")
        print("3. Get Stock Info")
        print("4. Quit")
        while True:
            selected = 0
            while True:
                selected = input("Number: ")
                try:
                    selected = int(selected)
                    break
                except:
                    print("Invalid Input")

            if selected == 1:
                self.setModel()
                while True:
                    val = self.model.run()
                    if val == 1:
                        break
                break
            elif selected == 4:
                return 1
            else:
                print("Invalid Input Try Again")

        quitVal = input("Quit App? [Y/N] ")
        if quitVal.upper() == 'Y':
            return 1
        else:
            return 0
        