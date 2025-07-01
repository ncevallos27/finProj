import os
import requests

class StockApp():
    def __init__(self):
        self.api = os.getenv("stockAPI")
        self.url = 'https://api.stockdata.org/v1/data/quote'

    def setAPI(self, key):
        self.api = key

    def run(self):
        print("\nStock Price App")
        print("Select An Option Below")
        print("1. Get Stock Price")
        #print("2. Search Stock")
        #print("3. See Info")
        print("4. Set API Key")
        print("5. Quit")

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
                self.getPrice()
                break
            elif selected == 4:
                newKey = input("Enter new API key: ")
                self.setAPI(newKey)
            elif selected == 5:
                return 1
            else:
                print("Not an Option")

        return 0
    
    def getPrice(self):
        print("\nStock Price")
        ticker = input("Enter a Ticker: ")

        r = requests.get(self.url, params={"api_token":str(self.api), "symbols": ticker.upper()})
        if r.json()['meta']['returned'] < 1:
            print(f'Invalid Ticker')
            return

        rawData = r.json()['data'][0]


        print(f'\n{rawData['name']} ({rawData['ticker']}) Stock Info')
        print(f'Price: {rawData['price']}')
        print(f'Open: {rawData['day_open']}')
        print(f'Low: {rawData['day_low']}   High: {rawData['day_high']}')
        print(f'Previous Close: {rawData['previous_close_price']}   Change: {rawData['day_change']}%')