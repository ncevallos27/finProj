from AppClass import App
import os                                                                                                                                                                                                      
from dotenv import load_dotenv
from pathlib import Path

def main():
    print("\nBlack-Scholes Option Pricing Model")
    load_dotenv(Path(".env"))
    instance = App()
    while True:
        val = instance.run()
        if val == 1:
            break
    
if __name__ == "__main__":
    main()