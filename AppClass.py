from BSModelClass import BSModel
from StockAppClass import StockApp

class App():
    def __init__(self, m=None, a=None):
        model = m
        app = a

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
                print("Not an Option")

    def run(self):
        print("\nMain Menu")
        print("Select Option Below")
        print("1. Run Option Pricing")
        print("2. Get Stock Info")
        print("3. Quit")
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
            elif selected == 2:
                self.app = StockApp()
                while True:
                    val = self.app.run()
                    if val == 1:
                        break
                break
            elif selected == 3:
                return 1
            else:
                print("Not an Option")

        return 0
        