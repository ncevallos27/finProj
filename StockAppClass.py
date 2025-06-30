import os

class StockApp():
    def __init__(self):
        self.api = os.getenv("stockAPI")

    def setAPI(self, key):
        self.api = key