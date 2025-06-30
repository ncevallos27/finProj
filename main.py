from AppClass import App

def main():
    print("\nBlack-Scholes Option Pricing Model")
    instance = App()
    while True:
        val = instance.run()
        if val == 1:
            break
    
if __name__ == "__main__":
    main()