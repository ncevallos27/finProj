import os

class SearchApp():
    def __init__(self):
        self.api = os.getenv("stockAPI")

    def setAPI(self, key):
        self.api = key